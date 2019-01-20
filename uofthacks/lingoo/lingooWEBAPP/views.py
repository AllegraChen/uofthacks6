from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from google.cloud import language
from google.cloud.language import enums, types
from lingooWEBAPP.forms import HomeForm
from lingooWEBAPP.lingle import get_blue, get_red, get_yellow
from lingooWEBAPP.split_article import find_sentences

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
            sentences = find_sentences(text)
            form = HomeForm()
            yellow_text = get_yellow(text)
            blue_text = get_blue(text)
            red_text = get_red(text)
            args = {'form': form, 'sentences': sentences, 'ytext': yellow_text, 'btext': blue_text, 'rtext': red_text}
            #args = {'form': form, 'num': num}
            return render(request, self.template_name, args)

        


    
    
