from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string

def home_view(request):
    """
    Take in a request
    Return HTML as a response
    """
    article_qs = Article.objects.all()
    article_obj = Article.objects.all().first()
    
    context = {
        "object_list": article_qs,
        "object": article_obj,
    }
    HTML_STRING = render_to_string("home_view.html",context=context)

    return HttpResponse(HTML_STRING) 