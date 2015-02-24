from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError
from django.core.context_processors import csrf

from ar.forms import ContactForm

def index(request):
    return render_to_response('index.html', RequestContext(request))

def commercial(request):
    return render_to_response('commercial.html', RequestContext(request))

def hometheatre(request):
    return render_to_response('hometheatre.html', RequestContext(request))

def residential(request):
    return render_to_response('residential.html', RequestContext(request))

def ssf(request):
    return render_to_response('ssf.html', RequestContext(request))

def contact(request):
    if request.POST:
        form = ContactForm(request.POST)

        if form.is_valid():
            try:
                send_mail(form.cleaned_data['subject'] + ' ' + form.cleaned_data['type_of_work'], form.cleaned_data['message'], 
                          form.cleaned_data['email'], ['jessehodge1987@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('thankyou.html')
        else:
            return render_to_response('contact.html', {'form': form})
    else:
        return render_to_response('contact.html', {'form': ContactForm()},
            RequestContext(request))

def thankyou(request):
    return render_to_response('thankyou.html', RequestContext(request))

def thankyou(request):
		return render_to_response('thankyou.html')
