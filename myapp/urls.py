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
    InventionListView,  # Assuming it's imported here
    InventionDetailView  # Assuming it's imported here
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
    path('invention/<int:pk>/', InventionDetailView.as_view(), name='invention-view'),
]