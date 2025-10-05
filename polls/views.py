from django.shortcuts import render
from .models import Question

def index(request):
    latest_questions = Question.objects.all().order_by('-pub_date')[:5]  # get last 5 questions
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)
