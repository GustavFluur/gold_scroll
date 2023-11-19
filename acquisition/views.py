from django.shortcuts import render

# Create your views here.
def acquisition_view(request):

    return render(request, 'acquisition/acquisition.html')