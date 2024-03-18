from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from .default_data import load_default_data
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Invention
from django.views.generic import DetailView

from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to my Django project!")

def home(request):
  return render(request, 'home.html')



def get_context_data(self, **kwargs):
  context = super().get_context_data(**kwargs)
  context.setdefault('title', self.default_title)
  return context







def function_view(request):
  context = {
      'page_title': 'Function-Based View',
      'page_heading': 'Welcome to the Function-Based View',
      'page_content': 'This is the content generated by the function-based view.',
  }
  return render(request, 'bootswatch.html', context)


#class from which all class based views inherit
class BaseView(TemplateView):
    default_title = 'My Website'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault('title', self.default_title)
        return context

class ClassView(BaseView):
    template_name = 'bootswatch.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Class-Based View',
            'page_heading': 'Welcome to the Class-Based View',
            'page_content': 'This is the content generated by the class-based view.',
        })
        return context 

class ThemeView(BaseView):
  template_name = 'theme.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # Add additional context data if needed
      return context

  def post(self, request, *args, **kwargs):
      theme = request.POST.get('theme')
      response = HttpResponseRedirect(reverse('theme'))
      response.set_cookie('theme', theme)
      return response


class FunnyView(BaseView):
  template_name = 'funny.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # Add additional context data if needed
      return context

  def post(self, request, *args, **kwargs):
      funny = request.POST.get('funny')
      response = HttpResponseRedirect(reverse('funny'))
      response.set_cookie('funny', funny)
      return response


class SummerView(BaseView):
  template_name = 'summer.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # Add additional context data if needed
      return context

  def post(self, request, *args, **kwargs):
      summer = request.POST.get('summer')
      response = HttpResponseRedirect(reverse('summer'))
      response.set_cookie('summer', summer)
      return response


class LearningView(BaseView):
  template_name = 'learning.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # This is a placeholder for additional context data that might be needed
      return context

  def post(self, request, *args, **kwargs):
      learning = request.POST.get('learning')
      response = HttpResponseRedirect(reverse('learning'))
      response.set_cookie('learning', learning)
      return response





def load_default_data_view(request):
    load_default_data()  # Call the load_default_data function
    return JsonResponse({'status': 'success'})


class InventionListView(ListView):
    model = Invention
    template_name = 'invention_list.html'
    context_object_name = 'inventions'



class InventionDetailView(DetailView):
    model = Invention
    template_name = 'invention_view.html'
    context_object_name = 'invention'
