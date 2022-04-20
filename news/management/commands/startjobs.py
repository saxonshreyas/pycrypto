import logging 

from lib2to3.pytree import Base
from django.core.management.base import BaseCommand

import feedparser
import re 
from dateutil import parser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger 
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
import content_aggregator.settings as settings


from news.models import Article

CLEANR = re.compile('<.*?>') # this is the regular expression that removes everything inside html tags and returns just the text

COINTELEGRAPH_FEED = "https://cointelegraph.com/rss"

logger = logging.getLogger(__name__)

def save_new_articles(feed):
    """
    Saves new articles to the database 

    Checks if the article GUID is already stored in the database and if not, then 
    parse the XML to add the new article to the database. 
    """
    def cleanhtml(raw_html):
        cleantext = re.sub(CLEANR, '', raw_html)
        return cleantext
    
    publisher_title = feed.channel.title
    
    for item in feed.entries:
        if not Article.objects.filter(uid = item.guid).exists():
            new_article = Article(
                title = item.title,
                description = cleanhtml(item.description),
                pub_date = parser.parse(item.published),
                link = item.link,
                publisher = publisher_title,
                uid = item.guid
            )
            new_article.save()

def fetch_cointelegraph_articles():
    """Fetches new articles from Coin Telegraph RSS"""
    _feed = feedparser.parse(COINTELEGRAPH_FEED)
    save_new_articles(_feed)

def delete_old_job_executions(max_age=604_800):
    """Deletes all apscheduler job execution logs older than max_age"""
    DjangoJobExecution.objects.delete_old_job_executions(max_age) # 604,800 seconds is equal to 1 week hence the chosen number 

class Command(BaseCommand):
    help = "Runs scheduler"

    def handle(self, *args, **options):
            scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
            scheduler.add_jobstore(DjangoJobStore(), "default")

            scheduler.add_job(
                fetch_cointelegraph_articles,
                trigger="interval",
                seconds=10, # in a production environment this should definitely be more than two minutes, can replace with hours = 12 to run every 12 hours 
                id="Cointelegraph",
                max_instances=1,
                replace_existing=True,
            )
            logger.info("Added job: CoinTelegraph")

            scheduler.add_job(
                delete_old_job_executions,
                trigger=CronTrigger(
                    day_of_week="mon", hour="00", minute="00"
                ),  # Midnight on Monday, before start of the next work week.
                id="Delete Old Job Executions",
                max_instances=1,
                replace_existing=True,
            )
            logger.info("Added weekly job: Delete Old Job Executions.")

            try:
                logger.info("Starting scheduler")
                scheduler.start()
            except KeyboardInterrupt:
                logger.info("Stopping Scheduler")
                scheduler.shutdown()
                logger.info("Scheduler has been shutdown")
    