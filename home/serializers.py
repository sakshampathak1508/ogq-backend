from rest_framework import serializers
from .models import *

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'

class VisionAndMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisionAndMission
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class SelectionProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectionProcess
        fields = '__all__'

class AreasOfSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasOfSupport
        fields = '__all__'

class PerformanceReportFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReportFiles
        fields = '__all__'

class AnnualReturnFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnnualReturnFiles
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CsrPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = CsrPolicy
        fields = '__all__'

class AnnoucementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annoucement
        fields = '__all__'

class OlympicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Olympic
        fields = '__all__'

class ParalympicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paralympic
        fields = '__all__'

class JuniorAthletesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JuniorAthletes
        fields = '__all__'

class OlympicResultPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OlympicResultPlayers
        fields = '__all__'

class OgqImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = OgqImpact
        fields = '__all__'

class TeamOgqIndiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamOgqIndia
        fields = '__all__'

class TeamOgqUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamOgqUs
        fields = '__all__'

class HomePageCarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageCarousel
        fields = '__all__'

class MedalStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedalStats
        fields = '__all__'

class AthleteStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteStats
        fields = '__all__'

class CountdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countdown
        fields = '__all__'

class SportsOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsOptions
        fields = '__all__'

class TeamPositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPositions
        fields = '__all__'

class OlympicNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OlympicNames
        fields = '__all__'