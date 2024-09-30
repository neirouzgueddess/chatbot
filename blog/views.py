# blog/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return HttpResponse('this is my first url')

def article(request, article_id):  # Corrected function name
    return render(request, 'blog/index.html', {'article_id': article_id})
def getResponse(request):  
    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)



from chatterbot.trainers import ChatterBotCorpusTrainer 
from chatterbot import ChatBot

# Create a new chat bot instance
chatbot = ChatBot(
    'ErisBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Train the chatbot using the ChatterBot corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')  # You can specify the language corpus you want

def get_response(request):
    user_message = request.GET.get('userMessage', None)
    if user_message:
        # Get a response from the chatbot
        bot_response = chatbot.get_response(user_message)
        return JsonResponse({'response': str(bot_response)})
    return JsonResponse({'response': 'I didn\'t understand that.'})
