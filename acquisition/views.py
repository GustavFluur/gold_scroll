from django.shortcuts import render, redirect

# Create your views here.
def acquisition_view(request):

    return render(request, 'acquisition/acquisition.html')



def add_to_acquisition(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    acquisition = request.session.get('acquisition', {})

    if item_id in list(acquisition.keys()):
        acquisition[item_id] += quantity
    else:    
        acquisition[item_id] = quantity
    
    request.session['acquisition'] = acquisition
    return redirect(redirect_url)
