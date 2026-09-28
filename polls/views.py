from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    questions = Question.objects.all()
    return HttpResponse(render(request, "index.html", context={"questions": questions}))

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", context={"question": question})


def vote(request,question_id):
    return HttpResponse("You are viewing question detail s%" % question_id)