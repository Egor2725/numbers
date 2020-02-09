from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from random import randint
from django.contrib.auth.forms import UserCreationForm


def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/core/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def check_user(request):
    user = request.user
    if user.is_authenticated:
        return show_number(request)
    else:
        return redirect('/login/')


def find_prime_numbers():
    list_of_prime = []
    for n in range(2, 501):
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            list_of_prime.append(n)
    return list_of_prime


def show_number(request):
    list_of_numbers = find_prime_numbers()
    random_number = list_of_numbers[randint(0, len(list_of_numbers)-1)]
    number = {
        'random_prime_number': random_number
    }

    return JsonResponse({'random_prime_number': random_number})
