from django.db import models


def upload_player_image(instance, filename):
    return '{}/{}'.format("Players", '%s.jpg')


class Player(models.Model):
    PLACE_CHOICES = (
        ('pakistan', 'PAKISTAN'),
        ('india', 'INDIA'),
        ('canada', 'CANADA'),
        ('Australia', 'AUSTRALIA'),
        ('dubai', 'DUBAI'),
    )
    name = models.CharField(max_length=250, default='SOME STRING')
    dob = models.DateField(null=True)
    birth_place = models.CharField(max_length=250, choices=PLACE_CHOICES, default='Select from drop down')
    squad_no = models.IntegerField()
    bowling_style = models.CharField(max_length=250)
    player_type = models.CharField(max_length=250)
    image = models.ImageField(upload_to=upload_player_image, null=True, blank=True)
    total_matches = models.IntegerField(default=0)
    description = models.CharField(max_length=1000, default='SOME STRING')
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    email = models.EmailField(max_length=250, default='example@gmail.com')
    phone_no = models.IntegerField(default=0)
    Is_keeper = models.CharField(max_length=250, default=0)

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
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

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
    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
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
