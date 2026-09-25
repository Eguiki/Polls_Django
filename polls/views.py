from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request,question_id):
    return HttpResponse("You are viewing question detail s%" % question_id)

def results(request,question_id):
    response = "You are viewing question detail s%"
    return HttpResponse(request % question_id)

def vote(request,question_id):
    return HttpResponse("You are viewing question detail s%" % question_id)