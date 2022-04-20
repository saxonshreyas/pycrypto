from django.shortcuts import render
from django.views.generic import ListView 
from .models import Article

# Create your views here.
class HomePageView(ListView):
    template_name = "index.html"

    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.filter().order_by("-pub_date")[:10] # this shows the 10 latest articles found in the database
        print(context["articles"])
        return context