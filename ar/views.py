from django.shortcuts import render, redirect
from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError
from forms import ContactForm

def index(request):
    return render(request, 'index.html')

def commercial(request):
    return render(request, 'commercial.html')

def hometheatre(request):
    return render(request, 'hometheatre.html')

def residential(request):
    return render(request, 'residential.html')

def ssf(request):
    return render(request, 'ssf.html')

def contact(request):
    if request.POST:
        form = ContactForm(request.POST)
    else:
        form = ContactForm()

    if form.is_valid():
        try:
            send_mail(form.cleaned_data['subject'] + ' ' + form.cleaned_data['type_of_work'], form.cleaned_data['message'],
                     form.cleaned_data['email'], ['jessehodge1987@gmail.com'])
        except BadHeaderError:
           return render('Invalid header found.')
        return redirect('thankyou.html')
    else:
        return render(request, 'contact.html', {'form': form})

def thankyou(request):
    return render(request, 'thankyou.html')

def thankyou(request):
		return render(request, 'thankyou.html')
