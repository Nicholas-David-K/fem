from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='home'),
    path('events/', views.EventList.as_view(), name='events'),
    path('chapter/<slug:slug>/', views.ChapterDetailView.as_view(), name='chapter'),
    path('sermons/founder-sermons/', views.FounderSermons.as_view(), name='founder-sermons'),
    path('about/<slug:slug>/', views.AboutUsDetailView.as_view(), name='about-us'),
    path('about/<slug:slug>/founder/', views.FounderDetailView.as_view(), name='founder'),
    path('giving/', views.GivingView.as_view(), name='giving'),

]