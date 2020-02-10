from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .utils import get_prime_number


@login_required
def show_number(request):
    random_number = get_prime_number()

    return JsonResponse({'number': random_number}, status=200)
