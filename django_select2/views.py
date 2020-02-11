from django.shortcuts import render


# Create your views here.
def select2(request):
    return render(request, 'django_select2/select2.html')
