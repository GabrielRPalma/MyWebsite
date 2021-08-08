from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView, FormView)
from .models import Standard, Subject, Lesson
# Create your views here.


class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/standards.html'

def tutorial(request):
    return render(request, 'curriculum/tutorial.html')

class SubjectListView(DetailView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/subjectList.html'

class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'curriculum/lessonList.html'

