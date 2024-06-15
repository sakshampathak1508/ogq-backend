from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *


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
            data = TeamOgqIndia.objects.all().order_by('-id')
            serializer = TeamOgqIndiaSerializer(data,many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TeamOgqUsView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            data = TeamOgqUs.objects.all().order_by('-id')
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
            data = OgqImpact.objects.all().order_by('-id')
            serializer = OgqImpactSerializer(data,many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AnnualReturnView(APIView):
    def get(self, request):
        try:
            data = AnnualReturnFiles.objects.all().order_by('-id')
            serializer = AnnualReturnFilesSerializer(data,many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AnnualReportView(APIView):
    def get(self, request):
        try:
            data = PerformanceReportFiles.objects.all().order_by('-id')
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
            data = Testimonials.objects.all()[0]
            serializer = TestimonialsSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OlympicsView(APIView):
    def get(self, request):
        try:
            sport = request.GET.get('sport', '')
            data = Olympic.objects.filter(sport=sport).order_by('-id')
            serializer = OlympicSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ParalympicView(APIView):
    def get(self, request):
        try:
            sport = request.GET.get('sport', '').lower()
            data = Paralympic.objects.filter(sport=sport).order_by('-id')
            serializer = ParalympicSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class JuniorView(APIView):
    def get(self, request):
        try:
            sport = request.GET.get('sport', '').lower()
            data = JuniorAthletes.objects.filter(sport=sport).order_by('-id')
            serializer = JuniorAthletesSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class OlympicResultView(APIView):
    def get(self, request):
        try:
            year = request.GET.get('year', '').lower()
            data = OlympicResultPlayers.objects.filter(olympic_year=year).order_by('-id')
            serializer = OlympicResultPlayersSerializer(data, many=True)
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
            data = Annoucement.objects.all().order_by('-id')[:5]
            serializer = AnnoucementSerializer(data, Many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CarouselView(APIView):
    def get(self, request):
        try:
            data = HomePageCarousel.objects.all().order_by('-id')[:5]
            serializer = HomePageCarouselSerializer(data, Many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SportsNavbarView(APIView):
    def get(self, request):
        try:
            olympics = [
                'archery',
                'athletics',
                'badminton', 
                'boxing',
                'shooting',
                'table',
                'weightlifting',
                'wrestling'
            ]
            paralympics = [
                'archery',
                'athletics',
                'badminton', 
                'canoe',
                'judo',
                'power_lifting',
                'shooting',
                'table tennis',
            ]
            junior = [
                'archery',
                'athletics',
                'badminton', 
                'boxing',
                'shooting',
                'table tennis',
                'wrestling'
            ]
            data = {
                'olympics': olympics,
                'paralympics': paralympics,
                'junior' : junior
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)