from django.shortcuts import render


def account(request):


    template = 'accounts/account.html'
    context = {}

    return render(request, template, context)