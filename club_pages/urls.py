from django.urls import path

from club_pages import views
from club_pages.views import index, fixtures_results, latest_news, home, team, detail, newsdetail, BaseView
from club_pages.views import members, about, ContactUsView

urlpatterns = [

    path('index', index, name='index'),
    path('members', members.as_view(), name='members'),
    path('about-us', about.as_view(), name='about-us'),
    path('contact-us', ContactUsView.as_view(), name='contactus'),
    path('fixtures_results', fixtures_results.as_view(), name='features_result'),
    path('latest_news', latest_news.as_view(), name='latest_news'),
    path('', home.as_view(), name='home'),
    path('team', team.as_view(), name='team'),
    path('detail/<int:pid>', detail.as_view(), name='detail'),
    path('newsdetail/<int:nid>', newsdetail.as_view(), name='news_detail'),
    path('success/', views.successView, name='success'),
    path('base',BaseView.as_view(),name='baseview')

]
