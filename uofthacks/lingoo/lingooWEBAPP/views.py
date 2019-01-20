from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from google.cloud import language
from google.cloud.language import enums, types

client = language.LanguageServiceClient()

# Create your views here.
def resultView(request):
    if request.POST['text']:
        text = request.POST['text']
        document = types.Document(
                   content=text,
                   type=enums.Document.Type.PLAIN_TEXT
                   )
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        message = "Sentiment: {}".format(sentiment.score)
        #message = 'You searched for %r' %request.POST['text']
    else:
        message = 'You submitted an empty form.'
    
    return HttpResponse(message)


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html')

class ResultPageView(TemplateView):
    def post(self, request, **kwargs):
        return render(request, 'results.html')

    
