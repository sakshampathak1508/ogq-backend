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
            data = Testimonials.objects.all().order_by('-id')
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

class InitiatePaymentAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = json.loads(request.body)
        name = data['name']
        amount = data['amount']
        email = data['email']
        pan_number = data['pan']
        phone_number = data['phone_number']

        key_id = 'rzp_live_OputbbGc4fa7vn'
        key_secret = 'BXSsqMrYkZV76Yp0MqTkgGO8'

        url = "https://api.razorpay.com/v1/orders"
        headers = {
            "Content-Type": "application/json",
        }
        auth = (key_id, key_secret)
        payload = {
            'amount': int(amount) * 100,
            'currency': 'INR',
            'receipt': "3456",
            'payment_capture': 1
        }
        response = requests.post(url, headers=headers, auth=auth, json=payload)

        return_data = response.json()
        return JsonResponse(return_data)


class EmailAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name', '')
        email = data.get('email', '')
        address = data.get('address', '')
        pan = data.get('pan', '')
        phone = data.get('phone', '')
        amount = data.get('amount', '')
        duration = data.get('duration', '')
        tenure = data.get('tenure', '')
        
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = 'smtp.example.com'
        EMAIL_PORT = 587
        EMAIL_USE_TLS = True
        EMAIL_HOST_USER = 'ogqbanking@gmail.com'
        if not name or not email or not address or not pan or not phone or not amount or not duration or not tenure:
            return Response({'error': 'Missing required fields'}, status=400)

        subject = f'New message on Donation (Recurring) from {name}'
        message = f'''
            Name: {name}
            Email: {email}
            Address: {address}
            PAN: {pan}
            Phone: {phone}
            Amount: {amount}
            Duration: {duration}
            Tenure: {tenure}
        '''
        try:
            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                [EMAIL_HOST_USER],
                fail_silently=False,
            )
            return Response({'message': 'Form submitted successfully and email sent'})
        except Exception as e:
            return Response({'error': str(e)}, status=500)

class CountdownView(APIView):
    def get(self, request):
        try:
            data = Countdown.objects.all().order_by('-id')[0]
            serializer = CountdownSerializer(data, Many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MedalStatsView(APIView):
    def get(self, request):
        try:
            data = MedalStats.objects.all()[0]
            serializer = MedalStatsSerializer(data, Many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AthleteStatsView(APIView):
    def get(self, request):
        try:
            data = AthleteStats.objects.all()[0]
            serializer = AthleteStatsSerializer(data, Many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)