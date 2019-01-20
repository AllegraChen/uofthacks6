from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from google.cloud import language
from google.cloud.language import enums, types
from lingooWEBAPP.forms import HomeForm
from lingle import set_text

client = language.LanguageServiceClient()

class HomePageView(TemplateView):
    template_name = 'index.html'
    
    def get(self, request, **kwargs):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = HomeForm()
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


    
