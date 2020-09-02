from .models import Article
from django import forms


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(
        help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

    def clean_message(self):
        message = self.cleaned_data['message']
        if "pizza" in message:
            raise forms.ValidationError(
                "On ne veut pas entendre parler de pizza !")

        return message

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if sujet and message:  # Est-ce que sujet et message sont valides ?
            if "pizza" in sujet and "pizza" in message:
                raise forms.ValidationError(
                    "Vous parlez de pizzas dans le sujet ET le message ? Non mais ho !"
                )
                self.add_error("message")
            return cleaned_data

# Direct forms from Article Models


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

# See : https://docs.djangoproject.com/en/3.1/ref/forms/fields/#built-in-field-classes
# See View contact


class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()
