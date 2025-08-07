from django.urls import path
from .views import *

app_name = 'cocktails'
urlpatterns = [
    path('', home, name='home'),
    path('search/', search_cocktail, name='search_cocktail'),
    path('drink/<str:drink_id>/', drink_detail, name='drink_detail')

    # The following line is added to ensure the URL for drink details is correctly named
    # This is useful for reverse URL resolution in templates
]