from django import forms

TYPE_OF_WORK_CHOICES = (
    ('Commercial', 'Commercial'),
    ('Residential', 'Residential'),
)

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    type_of_work = forms.ChoiceField(choices = TYPE_OF_WORK_CHOICES)
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
