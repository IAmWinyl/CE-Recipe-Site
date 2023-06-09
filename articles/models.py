from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from .utils import slugify_instance_title
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class ArticleQuerySet(models.QuerySet):
    def search(self,query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)
    
    def search(self,query=None):
        return self.get_queryset().search(query=query)
    
# Create your models here.
class Article(models.Model): 
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True,null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    objects = ArticleManager()

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"slug":self.slug})
 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save,sender=Article)

def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(article_post_save,sender=Article)