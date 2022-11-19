
from django.urls import path, include
from . import views

app_name = 'JKUAT CU'
urlpatterns = [
    path('', views.SnippetListView.as_view(), name='Ministries'),
    path('<int:pk>/', views.SnippetDetailView.as_view(), name='detail')
]
