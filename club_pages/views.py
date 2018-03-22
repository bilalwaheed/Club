import generic as generic
from django.shortcuts import render, render_to_response
from django.views import generic

# Create your views here.
from club_pages.models import Player, Fixture, LatestNews, SliderImages


class ContactUsView(generic.TemplateView):
    template_name = 'ContactUs.html'

def index(request):
    return render(request,'index.html', {})

class members(generic.TemplateView):
    template_name = 'Members.html'

class about(generic.TemplateView):
    template_name = 'About.html'

class fixtures_results(generic.TemplateView):
     model = Fixture
     template_name = 'Feature_Result.html'
     def get(self, request, *args, **kwargs):
         fixtures = Fixture.objects.all()
         t_20 = Fixture.objects.filter(fixture_type='t20');
         Test = Fixture.objects.filter(fixture_type='test');
         Oneday = Fixture.objects.filter(fixture_type='oneday');
         Other = Fixture.objects.filter(fixture_type='other');
         return render(request, self.template_name, {'fixtures': fixtures, 't_20':t_20,'Test':Test,'Oneday':Oneday })

class latest_news(generic.TemplateView):
    model = LatestNews
    template_name = 'Latest_News.html'
    def get(self, request, *args, **kwargs):
        news = LatestNews.objects.all()
        return render(request, self.template_name, {'news': news})


class home(generic.TemplateView):
    model = LatestNews
    template_name = 'Home.html'
    #render_to_response(template_name)
    def get(self, request, *args, **kwargs):
        news = LatestNews.objects.all()
        sliderImages = SliderImages.objects.all()
        return render(request, self.template_name, {'news': news,'sliderImages': sliderImages})


class team(generic.TemplateView):
    template_name = 'Team.html'
    # render_to_response(template_name)
    def get(self, request, *args, **kwargs):
        players = Player.objects.all()
        return  render(request, self.template_name,{'players':players})

class detail(generic.TemplateView):
    model = Player
    template_name = 'Player_Detail.html'

    def get(self, request, *args, **kwargs):
        pid = kwargs.get('pid')
        player_detail = Player.objects.get(id=pid)
        return render(request, self.template_name, {'player_detail': player_detail})



class newsdetail(generic.TemplateView):

    model = LatestNews

    template_name = 'News_Detail.html'

    def get(self, request, *args, **kwargs):
        nid = kwargs.get('nid')
        news_detail = LatestNews.objects.get(id=nid)
        news = LatestNews.objects.all()
        return render(request, self.template_name, {'news_detail': news_detail, 'news': news})

