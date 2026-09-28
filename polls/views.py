from django.db.models import F
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice


def index(request):
    questions = Question.objects.all()
    return HttpResponse(render(request, "index.html", context={"questions": questions}))

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", context={"question": question})


def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {"question": question, "error_message": "You did not select a choice"})
    else:
        selected_choice.votes = F('votes') +1
        selected_choice.save()
        return HttpResponseRedirect(reverse("detail", args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,)