import generic as generic
from django.shortcuts import render, render_to_response
from django.views import generic

# Create your views here.
from club_pages.models import Player


class ContactUsView(generic.TemplateView):
    template_name = 'ContactUs.html'
    render_to_response(template_name)

def index(request):
    return render(request,'index.html', {})

class members(generic.TemplateView):
    template_name = 'Members.html'
    render_to_response(template_name)

class about(generic.TemplateView):
    template_name = 'About.html'
    render_to_response(template_name)

class fixtures_results(generic.TemplateView):
    template_name = 'Feature_Result.html'
    render_to_response(template_name)

class latest_news(generic.TemplateView):
    template_name = 'Latest_News.html'
    render_to_response(template_name)

class home(generic.TemplateView):
    template_name = 'Home.html'
    render_to_response(template_name)

class team(generic.TemplateView):
    template_name = 'Team.html'
    # render_to_response(template_name)

    def get(self, request, *args, **kwargs):
        players = Player.objects.all()
        return  render(request, self.template_name,{'players':players})

class detail(generic.TemplateView):
    template_name = 'Player_Detail.html'
    render_to_response(template_name)
