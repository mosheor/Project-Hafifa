import random
import string


def rand_name(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))
