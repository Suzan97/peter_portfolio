from django.shortcuts import render,redirect
from django.conf import settings 
import os
from architect.models import *
from django.http import FileResponse
from django.core.mail import send_mail
# Create your views here.


def BASE(request):
    return render(request, 'base.html')

def HOME(request):
    project = Project.objects.all()
    category = Category.objects.all()

    context = {'project': project, 'category': category}
    return render(request, 'Main/home.html', context)

def Download_CV(request):
    cv_file_path = os.path.join(settings.MEDIA_ROOT, 'PWMola_CV.pdf')
    response = FileResponse(open(cv_file_path, 'rb'), as_attachment=True)
    return response

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_address = request.POST.get('email')
        message = request.POST.get('message')

        # Send email
        subject = f"Contact form submission from {name}"
        message = f"Name: {name}\nEmail: {email_address}\nMessage: {message}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.DEFAULT_FROM_EMAIL]  # Send email to your email address

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        # Redirect or render a thank-you page
        return redirect('home')  # Replace with the URL you want to redirect to