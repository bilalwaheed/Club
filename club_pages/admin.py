from django.contrib import admin
from .models import Player, Club, Team, Member, Tournament, Fixture, LatestNews,SliderImages,TopCategory


class FixtureAdmin(admin.ModelAdmin):
    model = Fixture
    list_display = ('time', 'date', 'team1', 'team2', 'venue')

class PlayersAdmin(admin.ModelAdmin):
    model = Player
    list_display = ('name', 'dob', 'birth_place', 'squad_no', 'type', 'bowling_style', 'player_type', 'image', 'total_matches', 'average')

class ClubAdmin(admin.ModelAdmin):
    model = Club
    list_display = ('name', 'city', 'club_history')


class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ('name', 'coach_name', 'total_member','Ranking')

class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display = ('name', 'Email')

class TournamentAdmin(admin.ModelAdmin):
    model = Tournament
    list_display = ('name', 'title')

class LatestNewsAdmin(admin.ModelAdmin):
    model = LatestNews
    list_display = ('description', 'title')

class TopCategoryAdmin(admin.ModelAdmin):
    model = TopCategory
    list_display = ('player', 'title')

admin.site.register(Player, PlayersAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Fixture, FixtureAdmin)
admin.site.register(LatestNews, LatestNewsAdmin)
admin.site.register(SliderImages)
admin.site.register(TopCategory, TopCategoryAdmin)