from django.urls import path
from django.contrib import admin
from myapp.views import (
  ClassView,
  FunnyView,
  LearningView,
  SummerView,
  ThemeView,
  function_view,
  home,
  index,
  load_default_data_view,
  InventionListView,
  InventionDetailView,
  InventionCreateView,
  InventionUpdateView,
  InventionDeleteView
)


urlpatterns = [
  path('', index, name='index'),
  path('admin/', admin.site.urls),
  path('home/', home, name='home'),
  path('funny/', FunnyView.as_view(), name='funny'),
  path('learning/', LearningView.as_view(), name='learning'),
  path('summer/', SummerView.as_view(), name='summer'),
  path('function/', function_view, name='function_view'),
  path('class/', ClassView.as_view(), name='class_view'),
  path('theme/', ThemeView.as_view(), name='theme'),
  path('load/', load_default_data_view, name='load_default_data'),
  path('inventions/', InventionListView.as_view(), name='invention-list'),
  path(
    'invention/<int:pk>/update/',
    InventionUpdateView.as_view(),
    name='update_invention'
  ),
  path(
    'invention/create/',
    InventionCreateView.as_view(),
    name='create_invention'
  ),
  path(
    'invention/<int:pk>/',
    InventionDetailView.as_view(),
    name='invention-view'
  ),
  # Ensure to include the path for InventionDeleteView, which was missing
  path(
    'invention/<int:pk>/delete/',
    InventionDeleteView.as_view(),
    name='delete_invention'
  ),
]