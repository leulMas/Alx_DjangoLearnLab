from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello! Welcome to the custom user model app.")
