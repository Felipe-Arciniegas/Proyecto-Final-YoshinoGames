from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    context = {}
    return render(request, 'store_games/home.html')

def store(request):
    url = 'http://127.0.0.1:5000/games'
    try:
        response = requests.get(url)

        if response.status_code == 200:
            
            games= response.json()
        else:
            print(f"Error en la solicitud: {response.status_code}")
            games= []
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e}")
        games=[]
    return render(request, 'store_games/store.html', {'games': games})

def wishlist(request):
    context = {}
    return render(request, 'store_games/wishlist.html')

def cart(request):
    url = 'http://127.0.0.1:5000/games'
    try:
        response = requests.get(url)

        if response.status_code == 200:
            
            games= response.json()
        else:
            print(f"Error en la solicitud: {response.status_code}")
            games= []
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e}")
        games=[]
    return render(request, 'store_games/cart.html', {'games': games})

def checkout(request):
    context = {}
    return render(request, 'store_games/checkout.html')



