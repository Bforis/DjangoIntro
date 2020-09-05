from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime
from .forms import ContactForm, NouveauContactForm
from .models import Contact
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


def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'contact.html', locals())


def nouveau_contact(request):  # View for files/form/upload
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True

    return render(request, 'contact.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })


def voir_contacts(request):
    return render(
        request,
        'voir_contacts.html',
        {'contacts': Contact.objects.all()}
    )
