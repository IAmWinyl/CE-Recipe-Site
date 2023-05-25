from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string

def home_view(request):
    """
    Take in a request
    Return HTML as a response
    """
    article_obj = Article.objects.get(id=2)
    article_qs = Article.objects.all()
    context = {
        "title" : article_obj.title,
        "content" : article_obj.content,
        "id" : article_obj.id,
        "object_list": article_qs,
    }
    HTML_STRING = render_to_string("home_view.html",context=context)

    return HttpResponse(HTML_STRING) 