from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from django.http import  JsonResponse, HttpResponse
# Create your views here.
def home(request):
    return redirect('search_cocktail')
def search_cocktail(request):
    query = request.GET.get('q', '')
    url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cocktails = data.get('drinks', [])
        return render(request, 'cocktails/search_results.html', {'query': query, 'cocktails': cocktails})
    else:
        return HttpResponse("Error fetching data from the cocktail API.", status=500)
def drink_detail(request, drink_id):
    url = f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink_id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        drink = data.get('drinks', [])[0] if data.get('drinks') else None
        ingredients = []
        for i in range(1, 4):
            ingredient = drink.get(f'strIngredient{i}')
            measure = drink.get(f'strMeasure{i}')
            if ingredient:
                ingredients.append({'ingredient': ingredient, 'measure': measure})
        return render(request, 'cocktails/drink_detail.html', {'drink': drink, 'ingredients': ingredients})
    return render(request, 'cocktails/drink_detail.html', {'drink': None, 'ingredients': []})