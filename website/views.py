from django.shortcuts import render
from django.utils import timezone
from website.forms import ContactForm, NewsletterForm
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = 'Anonymous'
            form.save()
            messages.success(request, 'Your message has been sent.')
        else:
            messages.error(request, 'Your message has not been sent.(Error)')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'website/contact.html', context)


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")
    form = NewsletterForm()
    context = {'form': form}
    return render(request, 'index.html', context)
