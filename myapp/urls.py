from django.urls import path
from myapp.views import ClassView, FunnyView, LearningView, SummerView, ThemeView, function_view, home, index

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('funny/', FunnyView.as_view(), name='funny'),
    path('learning/', LearningView.as_view(), name='learning'),
    path('summer/', SummerView.as_view(), name='summer'),
    path('function/', function_view, name='function_view'),
    path('class/', ClassView.as_view(), name='class_view'),
    path('theme/', ThemeView.as_view(), name='theme'),
]