from django.contrib import admin
from .models import Player, Club, Team, Member, Tournament, Fixture, LatestNews

admin.site.register(Player)
admin.site.register(Club)
admin.site.register(Team)
admin.site.register(Member)
admin.site.register(Tournament)
admin.site.register(Fixture)
admin.site.register(LatestNews)
