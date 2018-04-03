from django.db import models


def upload_player_image(instance, filename):
    return '{}/{}'.format("Players", '%s.jpg')


class Player(models.Model):
    name = models.CharField(max_length=250, default='SOME STRING')
    dob = models.DateField(null=True)
    birth_place = models.CharField(max_length=250)
    squad_no = models.IntegerField()
    type = models.CharField(max_length=250)
    # type = models.CharField(max_length=250)
    bowling_style = models.CharField(max_length=250)
    player_type = models.CharField(max_length=250)
    image = models.ImageField(upload_to=upload_player_image, null=True, blank=True)
    odi_matches = models.IntegerField(default=0)
    test_matches = models.IntegerField(default=0)
    total_matches = models.IntegerField(default=0)
    average = models.IntegerField(default=0)
    total_runs = models.IntegerField(default=0)
    total_wickets = models.IntegerField(default=0)
    catches = models.IntegerField(default=0)
    description = models.CharField(max_length=1000, default='SOME STRING')
    team = models.ForeignKey("Team", on_delete=models.CASCADE)

    # team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TopCategory(models.Model):
    title = models.CharField(max_length=250, default='Some String')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Club(models.Model):
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    club_history = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=250)
    coach_name = models.CharField(max_length=250)
    total_member = models.IntegerField()
    Ranking = models.IntegerField()
    logo = models.CharField(max_length=1000)
    slug = models.CharField(max_length=250)
    # player_detail = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=250)
    Email = models.EmailField()

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)


    def __str__(self):
        return self.name


class Fixture(models.Model):
    T20 = 't20'
    Test = 'test'
    OneDay = 'oneday'
    Other = 'other'

    FIXTURE_TYPE = (
        (T20, 'T20'),
        (Test, 'Test'),
        (OneDay, 'One Day'),
        (Other, 'Other')
    )
    time = models.TimeField()
    date = models.DateField(null=True)
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    # team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    team2 = models.CharField(max_length=250)
    venue = models.CharField(max_length=250)
    fixture_type = models.CharField(max_length=50, choices=FIXTURE_TYPE, default='Type')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class LatestNews(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to=upload_player_image, null=True, blank=True)

    def __str__(self):
        return self.title


class SliderImages(models.Model):
    image = models.ImageField(upload_to=upload_player_image, null=True, blank=True)

class UpCommingMatches(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField(null=True)
    team1 = models.CharField(max_length=250)
    team2 = models.CharField(max_length=250)
    time = models.TimeField()
