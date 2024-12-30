import json
import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny
from django.conf import settings
from django.http import JsonResponse
from .serializers import *
from .models import *
from django.utils import timezone

class VissionView(APIView):
    def get(self, request):
        try:
            data = VisionAndMission.objects.all()[0]
            serializer = VisionAndMissionSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class HistoryView(APIView):
    def get(self, request):
        try:
            data = History.objects.all()[0]
            serializer = HistorySerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TeamOgqIndiaView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            gr = request.GET.get('group', '').lower()
            data = TeamOgqIndia.objects.filter(group=gr).order_by('rank')
            serializer = TeamOgqIndiaSerializer(data,many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TeamOgqUsView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            data = TeamOgqUs.objects.all().order_by('rank')
            serializer = TeamOgqUsSerializer(data,many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContactView(APIView):
    def get(self, request):
        try:
            data = Contact.objects.all()[0]
            serializer = ContactSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AreasOfSupportView(APIView):
    def get(self, request):
        try:
            data = AreasOfSupport.objects.all()[0]
            serializer = AreasOfSupportSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class OgqImpactView(APIView):
    def get(self, request):
        try:
            data = OgqImpact.objects.all().order_by('rank')
            serializer = OgqImpactSerializer(data,many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AnnualReturnView(APIView):
    def get(self, request):
        try:
            data = AnnualReturnFiles.objects.all()
            serializer = AnnualReturnFilesSerializer(data,many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AnnualReportView(APIView):
    def get(self, request):
        try:
            data = PerformanceReportFiles.objects.all()
            serializer = PerformanceReportFilesSerializer(data,many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CsrPolicyView(APIView):
    def get(self, request):
        try:
            data = CsrPolicy.objects.all()[0]
            serializer = CsrPolicySerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SelectionView(APIView):
    def get(self, request):
        try:
            data = SelectionProcess.objects.all()[0]
            serializer = SelectionProcessSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestimonialView(APIView):
    def get(self, request):
        try:
            data = Testimonials.objects.all().order_by('rank')
            serializer = TestimonialsSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OlympicsView(APIView):
    def get(self, request):
        try:
            sport = request.GET.get('sport', '')
            data = Olympic.objects.filter(sport=sport).order_by('rank')
            serializer = OlympicSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ParalympicView(APIView):
    def get(self, request):
        try:
            sport = request.GET.get('sport', '').lower()
            data = Paralympic.objects.filter(sport=sport).order_by('rank')
            serializer = ParalympicSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class JuniorView(APIView):
    def get(self, request):
        try:
            sport = request.GET.get('sport', '').lower()
            data = JuniorAthletes.objects.filter(sport=sport).order_by('rank')
            serializer = JuniorAthletesSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DropdownView(APIView):
    def get(self, request):
        olympic_data_obj = OlympicNames.objects.all()
        team_data_obj = TeamPositions.objects.all()

        olympic_data = []
        team_data = []

        for i in olympic_data_obj:
            olympic_data.append(i.text)

        for j in team_data_obj:
            team_data.append(j.text)
        data = {
            'olympic_result' : olympic_data,
            'team_ogq_india_groups' : team_data
        }
        return Response(data, status=status.HTTP_200_OK)


class OlympicResultView(APIView):
    def get(self, request):
        try:
            year = request.GET.get('year', '').lower()
            data = OlympicResultPlayers.objects.filter(olympic_year=year).order_by('rank')
            serializer = OlympicResultPlayersSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ParalympicsResultView(APIView):
    def get(self, request):
        try:
            year = request.GET.get('year', '').lower()
            data = ParalympicResultPlayers.objects.filter(olympic_year=year).order_by('rank')
            serializer = ParalympicResultPlayersSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CategoryView(APIView):
    def get(self, request, *args, **kwargs):
        output_data = []
        cat = request.GET.get('cat', '')
        ty = request.GET.get('type','')
        num = request.GET.get('p', '')
        ans = int(num)*20
        if cat and num:
            if ty=='news':
                output_data = CardNewsSerializer(News.objects.filter(acbs_category=cat).order_by('-timestamp')[ans-20:ans],many=True).data
            elif ty=='event':
                output_data = EventCardSerializer(Event.objects.filter(acbs_category=cat).order_by('-start_date')[ans-20:ans],many=True).data
        return Response(output_data, status=status.HTTP_200_OK)

class AnnounceMentView(APIView):
    def get(self, request):
        try:
            data = Annoucement.objects.all()[:5]
            serializer = AnnoucementSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CarouselView(APIView):
    def get(self, request):
        try:
            data = HomePageCarousel.objects.all()[:5]
            serializer = HomePageCarouselSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SportsNavbarView(APIView):
    def get(self, request):
        try:
            olympics_sports = SportsOptions.objects.filter(event_type='olympics').order_by('text')
            para_sports = SportsOptions.objects.filter(event_type='paralympics').order_by('text')
            junior_sports = SportsOptions.objects.filter(event_type='junior').order_by('text')

            olympics = []
            paralympics = []
            junior = []

            for i in olympics_sports:
                olympics.append(i.text)

            for j in para_sports:
                paralympics.append(j.text)

            for k in junior_sports:
                junior.append(k.text)


            data = {
                'olympics': olympics,
                'paralympics': paralympics,
                'junior' : junior
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CountdownView(APIView):
    def get(self, request):
        try:
            current_date = timezone.now().date()
            data = Countdown.objects.filter(end_date__gt=current_date).order_by('start_date')
            serializer = CountdownSerializer(data,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MedalStatsView(APIView):
    def get(self, request):
        try:
            data = MedalStats.objects.all()[0]
            serializer = MedalStatsSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AthleteStatsView(APIView):
    def get(self, request):
        try:
            data = AthleteStats.objects.all()[0]
            serializer = AthleteStatsSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

