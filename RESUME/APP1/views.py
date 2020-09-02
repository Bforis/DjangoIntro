from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.


def view_base(request):
    #  All views must send an httpresponse.
    # Don't do this, html code must be in template.
    return HttpResponse("""
    <h1>First view.</h1>
    """)


def view_list(request, year, month=1):
    return HttpResponse('%s/%s' % (year, month))  # With parameters


def view_list2(request, month, year):
    return HttpResponse(
        "{0} {1}".format(month, year)
    )
