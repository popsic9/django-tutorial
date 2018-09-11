from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Chen Sun / 70efdf2e is the polls index.")