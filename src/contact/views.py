from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect

from .forms import contactForm
# Create your views here.
def contact(request):
    form = contactForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from MYSITE.com'
        message = '%s %s' %(comment, name) 
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail=(subject, message, emailFrom, emailTo)

        return HttpResponseRedirect('/')

    context = locals()
    template = 'contact.html'
    return render(request,template,context)