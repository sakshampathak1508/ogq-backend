from django.db import models
from django.utils import timezone

class Testimonials(models.Model):
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonial"

    def __str__(self):
        return "About Us"

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
    sport = models.CharField(choices=OLYMPICS_SPORTS,max_length=100,blank=True,null=True)
    name = models.CharField(max_length=200,default="")
    event = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to='image',blank=True,null=True)

    def __str__(self):
        return self.name


class Paralympic(models.Model):
    sport = models.CharField(choices=PARALYMPICS_SPORTS,max_length=100,blank=True,null=True)
    name = models.CharField(max_length=200,default="")
    event = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to='image',blank=True,null=True)

    def __str__(self):
        return self.name

class JuniorAthletes(models.Model):
    sport = models.CharField(choices=JUNIOR_SPORTS,max_length=100,blank=True,null=True)
    name = models.CharField(max_length=200,default="")
    event = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to='image',blank=True,null=True)

    class Meta:
        verbose_name = "Junior Scholoarship athletes"
        verbose_name_plural = "Junior Scholoarship athletes"

    def __str__(self):
        return self.name

RESULT_TEXT = (
    ('rio 2016','rio 2016'),
    ('london 2012','london 2012'),
)

class OlympicResultPlayers(models.Model):
    olympic_year = models.CharField(choices=RESULT_TEXT,max_length=100,blank=True,null=True)
    name = models.CharField(max_length=200,default="")
    caption = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to='image',blank=True,null=True)

    class Meta:
        verbose_name = "Olympic Results Players"
        verbose_name_plural = "Olympic Results Players"

    def __str__(self):
        return self.name


class TeamOgqIndia(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to='image',blank=True,null=True)
    joining_date = models.DateField(auto_now=True, blank=True, null=True)
    designation = models.CharField(max_length=200,blank=True,null=True)
    sporting_achivements = models.CharField(max_length=200,blank=True,null=True)
    qualification = models.CharField(max_length=200,blank=True,null=True)
    linkedin = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Team OGQ India"
        verbose_name_plural = "Team OGQ India"

    def __str__(self) -> str:
        return self.name

class TeamOgqUs(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to='image',blank=True,null=True)
    joining_date = models.DateField(auto_now=True, blank=True, null=True)
    designation = models.CharField(max_length=200,blank=True,null=True)
    sporting_achivements = models.CharField(max_length=200,blank=True,null=True)
    qualification = models.CharField(max_length=200,blank=True,null=True)
    linkedin = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Team OGQ US"
        verbose_name_plural = "Team OGQ US"

    def __str__(self) -> str:
        return self.name

class OgqImpact(models.Model):
    name = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to='image',blank=True,null=True)
    caption = models.CharField(max_length=200,default="")

    class Meta:
        verbose_name = "Olympic Impact Players"
        verbose_name_plural = "Olympic Impact Players"

    def __str__(self):
        return self.name


class HomePageCarousel(models.Model):
    name = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to='image',blank=True,null=True)

    class Meta:
        verbose_name = "Home Page Carousel"
        verbose_name_plural = "Home Page Carousel"

    def __str__(self):
        return self.name