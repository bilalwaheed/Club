from django.contrib import admin
from .models import Player, Club, Team, Tournament, Fixture, LatestNews,SliderImages,TopCategory


class FixtureAdmin(admin.ModelAdmin):
    model = Fixture
    list_display = ('time', 'date', 'team1', 'team2', 'venue')

class PlayersAdmin(admin.ModelAdmin):
    model = Player
    list_display = ('name', 'dob', 'birth_place', 'squad_no', 'bowling_style', 'player_type', 'image')

class ClubAdmin(admin.ModelAdmin):
    model = Club
    list_display = ('name', 'city', 'club_history')


class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ('name', 'coach_name')

# class MemberAdmin(admin.ModelAdmin):
#     model = Member
#     list_display = ('name', 'Email')

class TournamentAdmin(admin.ModelAdmin):
    model = Tournament
    list_display = ('name', 'title')

class LatestNewsAdmin(admin.ModelAdmin):
    model = LatestNews
    list_display = ('description', 'title')

class TopCategoryAdmin(admin.ModelAdmin):
    model = TopCategory
    list_display = ('player', 'title')

# class UpCommingMatchesAdmin(admin.ModelAdmin):
#     model = UpCommingMatches
#     list_display = ('date', 'title', 'team1', 'team2', 'time')

admin.site.register(Player, PlayersAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Team, TeamAdmin)
# admin.site.register(Member, MemberAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Fixture, FixtureAdmin)
admin.site.register(LatestNews, LatestNewsAdmin)
admin.site.register(SliderImages)
admin.site.register(TopCategory, TopCategoryAdmin)
# admin.site.register(UpCommingMatches, UpCommingMatchesAdmin)