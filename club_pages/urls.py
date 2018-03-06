from django.urls import path
from Club import settings
from club_pages.views import index, fixtures_results, latest_news, home ,team ,detail
from . import views
from django.conf import settings
from django.conf.urls.static import static
from club_pages.views import members, about, ContactUsView

urlpatterns = [
    # ... the rest of your URLconf goes here ...
    path('index',index, name='index'),
    path('members', members.as_view(), name='members'),
    path('about-us', about.as_view(), name='about-us'),
    path('contact-us', ContactUsView.as_view(), name='contactus'),
    path('fixtures_results', fixtures_results.as_view(), name='features_result'),
    path('latest_news', latest_news.as_view(), name='latest_news'),
    path('home', home.as_view(), name='home'),
    path('team', team.as_view(), name='team'),
    path('detail', detail.as_view(), name='detail')

    ]
