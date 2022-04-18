from urllib import response
from django.test import TestCase
from django.utils import timezone
from .models import Article
from django.urls.base import reverse

# Create your tests here.
class ArticleTests(TestCase):
    def setUp(self):
        self.sampleArticle = Article.objects.create(
            title = "Sample Crypto News Article",
            description = "Sample Crypto News Article about Bitcoin or something",
            pub_date = timezone.now(),
            link = "https://article.com",
            publisher = "Sample Publisher",
            uid = "de194720-7b4c-49e2-a05f-432436d3fetr"
        )
    
    """
    Test to see if article content is correctly added to the database
    """
    def test_articleContent(self):
        self.assertEqual(self.sampleArticle.title, "Sample Crypto News Article"),
        self.assertEqual(self.sampleArticle.uid, "de194720-7b4c-49e2-a05f-432436d3fetr"),
        self.assertEqual(self.sampleArticle.link, "https://article.com")

    """
    Test to see if page appropriately loads (response code 200)
    """
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    """
    Test to see if home page is using the correct html template
    """
    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse("homepage")) # the argument to the reverse function is equal to the name argument used in the urls.py of the same folder
        self.assertTemplateUsed(response, "index.html")

    """
    Test if the home page lists out the right contents 
    """
    
    
