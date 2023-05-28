from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Article
from .forms import ArticleForm

def article_search_view(request):
    article_obj = None
    q = request.GET.get("q")
    object_list = Article.objects.search(query=q)
        
    context = {
        "object_list" : object_list
    }
    return render(request,"articles/search.html",context=context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        article_obj = form.save()
        context["object"] = article_obj
        context["created"] = True
    
    return render(request,"articles/create.html",context=context)

# Create your views here.
def article_detail_view(request, slug=None):
    article_obj = None
    context = {}
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.get(slug=slug).first()
        except:
            raise Http404
    context = {
        "object" : article_obj,
    }

    return render(request,"articles/details.html",context=context)