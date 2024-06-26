from django.shortcuts import render,get_object_or_404,redirect
from .models import Restaurant
import json


def search(request):
    query = request.GET.get('q', '')
    results = []

#Handling JSON data
    if query:
        restaurants = Restaurant.objects.all()
        for restaurant in restaurants:
            try:
                items = json.loads(restaurant.Item)
                for dish, price in items.items():
                    if query.lower() in dish.lower():
                        results.append({
                            'restaurant_name': restaurant.name,
                            'restaurant_location': restaurant.location,
                            'dish': dish,
                            'price': price,
                        })
            except json.JSONDecodeError:
                continue

    return render(request, 'restaurant/search.html', {'results': results, 'query': query})