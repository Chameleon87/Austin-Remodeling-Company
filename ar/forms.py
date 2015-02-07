from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    type_of_work = forms.ChoiceField(choices = (('Commercial', 'Commercial'), ('Residential', 'Residential')))
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
