from random import choice


def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


def get_prime_number():
    return choice(
        list(
            filter(
                is_prime,
                range(2, 500)
            )
        )
    )
