from django.shortcuts import render
from django.http import JsonResponse

from random import randint


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
    # return render(request, 'base.html', {'number': random_number})
    return JsonResponse({'random_prime_number': random_number})
