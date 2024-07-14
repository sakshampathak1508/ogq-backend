from django.db import models
from django.utils import timezone

class Testimonials(models.Model):
    name = models.CharField(max_length=200,default="")
    caption = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to='image',blank=True,null=True)
    extra_info = models.TextField(blank=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonial"

    def __str__(self):
        return f"Testimonial of {self.name}"

class VisionAndMission(models.Model):
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = "Vision And Mission"
        verbose_name_plural = "Vision And Mission"

    def __str__(self):
        return "Vision And Mission"

class History(models.Model):
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = "History"
        verbose_name_plural = "History"

    def __str__(self):
        return "History"

class SelectionProcess(models.Model):
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = "Selection Process"
        verbose_name_plural = "Selection Process"

    def __str__(self):
        return "Selection Process"

class AreasOfSupport(models.Model):
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = "Areas Of Support"
        verbose_name_plural = "Areas Of Support"

    def __str__(self):
        return "Areas Of Support"


class PerformanceReportFiles(models.Model):
    name = models.CharField(max_length=200,default="")
    file = models.FileField(upload_to='home/files',blank=True,null=True)

    class Meta:
        verbose_name = "Performance Report Files"
        verbose_name_plural = "Performance Report Files"

    def __str__(self):
        return self.name

class AnnualReturnFiles(models.Model):
    name = models.CharField(max_length=200,default="")
    file = models.FileField(upload_to='home/files',blank=True,null=True)

    class Meta:
        verbose_name = "Annual Return Files"
        verbose_name_plural = "Annual Return Files"

    def __str__(self):
        return self.name

class CsrPolicy(models.Model):
    file = models.FileField(upload_to='home/files',blank=True,null=True)

    class Meta:
        verbose_name = "CSR Policy"
        verbose_name_plural = "CSR Policy"

    def __str__(self):
        return "CSR Policy"

class Contact(models.Model):
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return 'contact us details'

class Annoucement(models.Model):
    image = models.ImageField(upload_to='image',blank=True,null=True)
    url = models.URLField(max_length=200,blank=True,null=True)

    def __str__(self):
        return f"Announcement {self.id}"

OLYMPICS_SPORTS = (
    ('archery','archery'),
    ('athletics','athletics'),
    ('badminton','badminton'),
    ('boxing','boxing'),
    ('shooting','shooting'),
    ('table tennis','table tennis'),
    ('weightlifting','weightlifting'),
    ('wrestling','wrestling'),
)

PARALYMPICS_SPORTS = (
    ('archery','archery'),
    ('athletics','athletics'),
    ('badminton','badminton'),
    ('canoe','canoe'),
    ('judo','judo'),
    ('power lifting','power lifting'),
    ('shooting','shooting'),
    ('table tennis','table tennis'),
)

JUNIOR_SPORTS = (
    ('archery','archery'),
    ('athletics','athletics'),
    ('badminton','badminton'),
    ('boxing','boxing'),
    ('shooting','shooting'),
    ('table tennis','table tennis'),
    ('wrestling','wrestling')
)

class Olympic(models.Model):
    sport = models.CharField(max_length=100,blank=True,null=True)
    name = models.CharField(max_length=200,default="")
    event = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to='image',blank=True,null=True)

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(Olympic, self).__init__(*args, **kwargs)
        self._meta.get_field('sport').choices = [(pos.text, pos.text) for pos in SportsOptions.objects.filter(event_type='olympics')]


class Paralympic(models.Model):
    sport = models.CharField(max_length=100,blank=True,null=True)
    name = models.CharField(max_length=200,default="")
    event = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to='image',blank=True,null=True)

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(Paralympic, self).__init__(*args, **kwargs)
        self._meta.get_field('sport').choices = [(pos.text, pos.text) for pos in SportsOptions.objects.filter(event_type='paralympics')]

class JuniorAthletes(models.Model):
    sport = models.CharField(max_length=100,blank=True,null=True)
    name = models.CharField(max_length=200,default="")
    event = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to='image',blank=True,null=True)

    class Meta:
        verbose_name = "Junior Scholoarship athletes"
        verbose_name_plural = "Junior Scholoarship athletes"

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(JuniorAthletes, self).__init__(*args, **kwargs)
        self._meta.get_field('sport').choices = [(pos.text, pos.text) for pos in SportsOptions.objects.filter(event_type='junior')]

RESULT_TEXT = (
    ('paris 2024','paris 2024'),
    ('rio 2016','rio 2016'),
    ('london 2012','london 2012'),
)

class OlympicResultPlayers(models.Model):
    olympic_year = models.CharField(max_length=100,blank=True,null=True)
    name = models.CharField(max_length=200,default="")
    caption = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to='image',blank=True,null=True)

    class Meta:
        verbose_name = "Olympic Results Players"
        verbose_name_plural = "Olympic Results Players"

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(OlympicResultPlayers, self).__init__(*args, **kwargs)
        self._meta.get_field('olympic_year').choices = [(pos.text, pos.text) for pos in OlympicNames.objects.all()]

GROUPS = (
    ('board of directors','board of directors'),
    ('executive committee','executive committee'),
    ('management','management'),
    ('sports science','sports science'),
    ('ogq ambasdors','ogq ambassadors'),
    ('chapter heads','chapter heads'),
)

class TeamOgqIndia(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to='image',blank=True,null=True)
    group = models.CharField(max_length=100,blank=True,null=True)
    joining_date = models.DateField(auto_now=True, blank=True, null=True)
    designation = models.CharField(max_length=200,blank=True,null=True)
    sporting_achivements = models.CharField(max_length=200,blank=True,null=True)
    qualification = models.CharField(max_length=200,blank=True,null=True)
    linkedin = models.URLField(blank=True, null=True)
    about_them = models.TextField(blank=True)
    rank = models.BigIntegerField(default=1)

    class Meta:
        verbose_name = "Team OGQ India"
        verbose_name_plural = "Team OGQ India"

    def __str__(self) -> str:
        return self.name

    def __init__(self, *args, **kwargs):
        super(TeamOgqIndia, self).__init__(*args, **kwargs)
        self._meta.get_field('group').choices = [(pos.text, pos.text) for pos in TeamPositions.objects.all()]

class TeamOgqUs(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to='image',blank=True,null=True)
    joining_date = models.DateField(auto_now=True, blank=True, null=True)
    designation = models.CharField(max_length=200,blank=True,null=True)
    sporting_achivements = models.CharField(max_length=200,blank=True,null=True)
    qualification = models.CharField(max_length=200,blank=True,null=True)
    linkedin = models.URLField(blank=True, null=True)
    about_them = models.TextField(blank=True)

    class Meta:
        verbose_name = "Team OGQ US"
        verbose_name_plural = "Team OGQ US"

    def __str__(self) -> str:
        return self.name

class OgqImpact(models.Model):
    name = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to='image',blank=True,null=True)
    caption = models.CharField(max_length=200,default="")
    about_them = models.TextField(blank=True)

    class Meta:
        verbose_name = "Olympic Impact Players"
        verbose_name_plural = "Olympic Impact Players"

    def __str__(self):
        return self.name


class HomePageCarousel(models.Model):
    title = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to='image',blank=True,null=True)

    class Meta:
        verbose_name = "Home Page Carousel"
        verbose_name_plural = "Home Page Carousel"

    def __str__(self):
        return self.title

class MedalStats(models.Model):
    olympics = models.CharField(max_length=20,default="")
    world_championships = models.CharField(max_length=20,default="")
    asian_games = models.CharField(max_length=20,default="")
    asian_games = models.CharField(max_length=20,default="")
    commonwealth_games = models.CharField(max_length=20,default="")
    youth_olympics = models.CharField(max_length=20,default="")
    junior_world_championships = models.CharField(max_length=20,default="")
    paralympics = models.CharField(max_length=20,default="")

    class Meta:
        verbose_name = "Medal Stats"
        verbose_name_plural = "Medal Stats"

    def __str__(self):
        return "Medal Stats"

class AthleteStats(models.Model):

    total_athletes = models.CharField(max_length=20,default="")
    senior_athletes = models.CharField(max_length=20,default="")
    junior_athletes = models.CharField(max_length=20,default="")
    para_athletes = models.CharField(max_length=20,default="")

    class Meta:
        verbose_name = "Athlete Stats"
        verbose_name_plural = "Athlete Stats"

    def __str__(self):
        return "Athlete Stats"

class Countdown(models.Model):

    text = models.CharField(max_length=20,default="")
    extra_info = models.TextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


    class Meta:
        verbose_name = "Countdown"
        verbose_name_plural = "Countdown"

    def __str__(self):
        return self.text

SPORTS = (
    ('olympics','olympics'),
    ('paralympics','paralympics'),
    ('junior','junior')
)
class SportsOptions(models.Model):
    text = models.CharField(max_length=100,default="")
    event_type = models.CharField(choices=SPORTS,max_length=100,default="")
    class Meta:
        verbose_name = "Sport options"
        verbose_name_plural = "Sport options"

    def __str__(self):
        return f"{self.text} added in category {self.event_type}"

class TeamPositions(models.Model):
    text = models.CharField(max_length=100,default="")

    class Meta:
        verbose_name = "Team Position options"
        verbose_name_plural = "Team Position options"

    def __str__(self):
        return self.text

class OlympicNames(models.Model):
    text = models.CharField(max_length=100,default="")

    class Meta:
        verbose_name = "Add olympics"
        verbose_name_plural = "Add olympics"

    def __str__(self):
        return self.text