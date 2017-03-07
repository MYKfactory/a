from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import TemplateView
from datetime import datetime
from django.http import HttpResponse
from .models import Person, Category, ResistedTodo

def index(request):
    latest_person_list = Person.objects.all()
    latest_category_list = Category.objects.all()
    latest_todo_list = ResistedTodo.objects.all()
#    t = loader.get_template('person/index.html')
#    c = Context({
#        'latest_poll_list': latest_poll_list,
#    })
    return render_to_response('summary/index.html',
                              {'latest_person_list': latest_person_list,'latest_category_list': latest_category_list,'latest_todo_list': latest_todo_list})

def category_detail(request, question_id):
    p = get_object_or_404(Category, pk=question_id)
    return render_to_response('category/detail.html', {'category': p})

def person_detail(request, question_id):
    p = get_object_or_404(Person, pk=question_id)
    return render_to_response('person/detail.html', {'person': p})

def todo_detail(request, question_id):
    p = get_object_or_404(ResistedTodo, pk=question_id)
    return render_to_response('todo/detail.html', {'todo': p})

def results(request, question_id):
    response = "You've looiking at rth resuluts of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("yo've boting on question %s." % question_id)
