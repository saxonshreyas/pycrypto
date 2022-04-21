from django.shortcuts import render
from django.views.generic import ListView 
from .models import Article

# parsing data from client 
from rest_framework.parsers import JSONParser
# bypass needing to have a csrf token (might need to change this when thinking about login)
from django.views.decorators.csrf import csrf_exempt
# for sending response to client 
from django.http import HttpResponse, JsonResponse
# API Definition for Article 
from .serializers import ArticleSerializer

# Create your views here.
class HomePageView(ListView):
    template_name = "index.html"

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.filter().order_by("-pub_date")[:10] # this shows the 10 latest articles found in the database
        print(context["articles"])
        return context

@csrf_exempt
def articles(request):
    '''
    Retrieve all article metadata
    '''
    if (request.method == 'GET'):
        # get queryset 
        articles = Article.objects.filter().order_by("-pub_date")[:10] # shows the 10 latest articles found in the database 
        # serialize the article data
        serializer = ArticleSerializer(articles, many = True)
        # return a JSON Response 
        return JsonResponse(serializer.data, safe = False)
    elif (request.method == 'POST'):
        # parse incoming information 
        data = JSONParser().parse(request)
        # instantiate with serializer
        serializer = ArticleSerializer(data = data)
        # check if sent infomraiton is okay 
        if (serializer.is_valid()):
            serializer.save() # save data to database 
            return JsonResponse(serializer.data, status=201) # provide JSON Response with saved data 
        return JsonResponse(serializer.errors, status=400) # provide JSON response with necessary error information 