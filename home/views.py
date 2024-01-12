from django.shortcuts import render, redirect
from django.views import View
from .models import Drink, Category, About, Contact
from django.contrib import messages
# Create your views here.


class HomeView(View):

    def get(self, request):
        cold_drinks = Drink.objects.filter(category=1)
        hot_drinks = Drink.objects.filter(category=2)
        fruit_drinks = Drink.objects.filter(category=3)
        special_drinks = Drink.objects.filter(category=4)
        about = About.objects.all().order_by('?')

        return render(request, 'home/index.html', {'cold_drinks': cold_drinks, 'hot_drinks': hot_drinks,
                                                   'fruit_drinks': fruit_drinks, 'special_drinks': special_drinks
                                                   , 'about': about})

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Message sent successfully', 'success')
        return redirect('home:home')




