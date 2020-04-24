from django.shortcuts import render
from first_app.models import topics,webPage,accessRecord
from . import forms
# Create your views here.

def index(request):
    webpages_list = accessRecord.objects.order_by('date')
    my_dict = {'access_records':webpages_list}
    return render(request, 'first_app/index.html', context=my_dict)

def baseForm(request):
    form = forms.user()
    if request.method == "POST":
        form = forms.user(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('error form invalid...')
    return render(request,'first_app/basic_form.html', context={'form': form})
