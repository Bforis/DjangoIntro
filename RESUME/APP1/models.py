from django.db import models
from django.utils import timezone
# Create your models here.
# Example of blog with articles etc...


class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Date de parution")
    # link to the another models (categorie)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    """
    CASCADE : en cas de suppression de la catégorie, tous les articles ayant cette catégorie seront également supprimés (provoquant une cascade de suppression) ;

    SET_NULL : vide le champ  categorie  de chaque objet si la valeur étrangère était supprimée (il faut que le champ accepte les valeurs vides, bien sûr) ;

    PROTECT : empêche de supprimer une valeur si elle est utilisée, via une exception Python.

    """

    # See reference to CharField etc... : https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types

    class Meta:
        verbose_name = "article"
        ordering = ['date']

    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.titre


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.nom
