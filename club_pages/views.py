from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from Club import settings
# Create your views here.
from club_pages.models import Player, Fixture, LatestNews, SliderImages, TopCategory, Team, DynamicData, Sponser, \
    FixtureType
from club_pages.utils import get_base_data
from .forms import ContactForm


class ContactUsView(generic.TemplateView):
    template_name = 'ContactUs.html'

    def post(self, request):
        # import pdb;pdb.set_trace()
        if request.method == 'GET':
            form = ContactForm()
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                msg = form.cleaned_data['message']
                name = form.cleaned_data['name']
                # message = 'This is message'
                message = "Name: " + name + "\n" + "From: " + from_email + "\n" + "Subject: " + subject + "\n" + "Message: " + msg
                try:
                    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER, ],
                              fail_silently=False, )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('contactus')
        context = get_base_data()
        context['form'] = form
        return render(request, "contactUs.html", context)

    def get(self, request, *args, **kwargs):
        context = get_base_data()
        return render(request, self.template_name, context)


def index(request):
    return render(request, 'index.html', {})


class members(generic.TemplateView):
    template_name = 'Members.html'


class about(generic.TemplateView):
    model = DynamicData
    template_name = 'About.html'

    def get(self, request, *args, **kwargs):
        dynamicdata = DynamicData.objects.filter(page_data=DynamicData.ABOUT).first()
        context = get_base_data()
        context['about_text'] = dynamicdata
        return render(request, self.template_name, context)


class fixtures_results(generic.TemplateView):
    model = Fixture
    template_name = 'Feature_Result.html'

    def get(self, request, *args, **kwargs):
        fixtures = Fixture.objects.all().order_by('date')
        context = get_base_data()
        context['fixtures'] = fixtures
        context['fixture_types'] = FixtureType.objects.all()
        return render(request, self.template_name, context)


class latest_news(generic.TemplateView):
    model = LatestNews
    template_name = 'Latest_News.html'

    def get(self, request, *args, **kwargs):
        news = LatestNews.objects.all()
        context = get_base_data()
        context['news'] = news
        return render(request, self.template_name, context)


class home(generic.TemplateView):
    model = LatestNews, Fixture, DynamicData
    template_name = 'Home.html'

    def get(self, request, *args, **kwargs):
        news = LatestNews.objects.all()
        sliderImages = SliderImages.objects.all()
        top_category = TopCategory.objects.all()
        dynamicdata = DynamicData.objects.filter(page_data=DynamicData.HOME).first()
        upcomming_mathes = Fixture.objects.filter(date__gt=timezone.now().date()).order_by('date')[:3]

        context = get_base_data()
        context['news'] = news
        context['sliderImages'] = sliderImages
        context['top_category'] = top_category
        context['home_text'] = dynamicdata
        context['upcomming_mathes'] = upcomming_mathes
        return render(request, self.template_name, context)


class team(generic.TemplateView):
    template_name = 'Team.html'

    def get(self, request, *args, **kwargs):
        players = Player.objects.all()
        first_team = Team.objects.all()[:1]
        teams = Team.objects.all()[0:]
        context = get_base_data()
        context['players'] = players
        context['first_team'] = first_team
        context['teams'] = teams
        return render(request, self.template_name, context)


class detail(generic.TemplateView):
    model = Player
    template_name = 'Player_Detail.html'

    def get(self, request, *args, **kwargs):
        pid = kwargs.get('pid')
        player_detail = Player.objects.get(id=pid)
        context = get_base_data()
        context['player_detail'] = player_detail
        return render(request, self.template_name, context)


class newsdetail(generic.TemplateView):
    model = LatestNews

    template_name = 'News_Detail.html'

    def get(self, request, *args, **kwargs):
        nid = kwargs.get('nid')
        news_detail = LatestNews.objects.get(id=nid)
        news = LatestNews.objects.all()
        context = get_base_data()
        context['news_detail'] = news_detail
        context['news'] = news

        return render(request, self.template_name, context)


class topcategory(generic.TemplateView):
    model = TopCategory
    template_name = 'Home.html'

    def get(self, request, *args, **kwargs):
        top_category = TopCategory.objects.all()
        context = get_base_data()
        context['top_category'] = top_category
        return render(request, self.template_name, context)


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
