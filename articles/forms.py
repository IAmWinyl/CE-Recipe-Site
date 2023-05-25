from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title",f"\"{title}\" already exists. Please choose a different title.")
        return data
    
class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data # dict
        title = cleaned_data.get("title")
        if "office" in title.lower():
            self.add_error("title","Title cannot contain the word \"office\".")
        return cleaned_data