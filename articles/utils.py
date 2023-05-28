import random
from django.utils.text import slugify

def slugify_instance_title(instance, save=False):
    slug = slugify(instance.title)

    # NOTE: This will run forever if there are 8999 instances created of one article
    klass = instance.__class__
    randNum = random.randrange(1000,9999)
    while klass.objects.filter(slug=(slug+"-"+str(randNum))).exclude(id=instance.id).exists():             
        randNum = random.randrange(1000,9999)

    instance.slug = f"{slug}-{str(randNum)}"

    if save:
        instance.save()
        
    return instance
