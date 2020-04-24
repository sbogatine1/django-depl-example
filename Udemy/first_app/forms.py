from django import forms
from django.forms import ModelForm
from first_app.models import topics, webPage


class userForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


    # class meta:
    #     model = topics
    #     fields = '__all__'
class user(forms.ModelForm):
    class Meta:
        model = webPage
        fields = '__all__'
