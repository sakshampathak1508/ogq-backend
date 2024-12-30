from django.urls import path
from .views import *

urlpatterns = [
    path('vission', VissionView.as_view()),
    path('history', HistoryView.as_view()),
    path('team_ogq_india', TeamOgqIndiaView.as_view()),
    path('team_ogq_us', TeamOgqUsView.as_view()),
    path('contact', ContactView.as_view()),
    path('areas_of_support', AreasOfSupportView.as_view()),
    path('ogq_impact', OgqImpactView.as_view()),
    path('annual_return', AnnualReturnView.as_view()),
    path('annual_report', AnnualReportView.as_view()),
    path('csr', CsrPolicyView.as_view()),
    path('selection', SelectionView.as_view()),
    path('testimonial', TestimonialView.as_view()),
    path('olympics', OlympicsView.as_view()),
    path('paralympics', ParalympicView.as_view()),
    path('junior', JuniorView.as_view()),
    path('olympics_result', OlympicResultView.as_view()),
    path('paralympics_result', ParalympicsResultView.as_view()),
    path('announcement', AnnounceMentView.as_view()),
    path('home_carousel', CarouselView.as_view()),
    path('sports_in_navbar', SportsNavbarView.as_view()),
    path('countdown', CountdownView.as_view()),
    path('medal_stats', MedalStatsView.as_view()),
    path('athlete_stats', AthleteStatsView.as_view()),
    path('dropdown', DropdownView.as_view()),
]