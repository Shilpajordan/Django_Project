from django.urls import path
from .views import CountryLanguageView

urlpatterns = [
    path('api/country-language/', CountryLanguageView.as_view(), name='country_language'),
]