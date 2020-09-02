from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime

# Create your views here.
# request : initial HTTP request
# VIEWS


def view_base(request):
    #  All views must send an httpresponse.
    # Don't do this, html code must be in template.
    return HttpResponse("""
    <h1>First view.</h1>
    """)


def view_date(request, month, year):
    return HttpResponse(
        "{0} {1}".format(month, year)
    )

# Auto redirection with Http404


def view_list(request, id_list):
    if id_list > 100:
        raise Http404

    return redirect(view_redirect)


def view_redirect(request):
    return HttpResponse("Redirection")

# VIEWS + TEMPLATES
# Path to the templates folder is in settings.py


def today_date(request):
    return render(request, 'date.html', {'date': datetime.now()})


def addition(request, n1, n2):
    total = n1 + n2

    return render(request, 'add.html', locals())
