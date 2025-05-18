from django.shortcuts import render,redirect
from datetime import datetime

def home(request):
    return render(request, 'home.html', {'now': datetime.now()})

def about(request):
    return render(request, 'about.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject', 'No Subject')
        message = request.POST.get('message')

        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject=subject,
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['madinatululumhifzulquran@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except:
            messages.error(request, "Failed to send the message. Please try again later.")

        return redirect('contact')  # Redirect to the same page

    return render(request, 'contact.html')  # Render your contact page


def courses(request):
    return render(request, 'courses.html')
# core/views.py
from django.core.mail import send_mail
from django.contrib import messages
from .forms import AdmissionForm

def admission(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            subject = "New Admission Application"
            body = (
                f"Student Name: {form.cleaned_data['student_name']}\n"
                f"Father's Name: {form.cleaned_data['father_name']}\n"
                f"Age: {form.cleaned_data['age']}\n"
                f"Course: {form.cleaned_data['course']}\n"
                f"Address: {form.cleaned_data['address']}\n"
                f"Phone: {form.cleaned_data['phone']}\n"
                f"Email: {form.cleaned_data['email'] or 'N/A'}\n"
            )
            send_mail(
                subject,
                body,
                'madinatululumhifzulquran@gmail.com',        # From email
                ['madinatululumhifzulquran@gmail.com'],      # To madrasa email
                fail_silently=False,
            )
            messages.success(request, "Your application has been submitted successfully.")
            return redirect('admission')
    else:
        form = AdmissionForm()
    return render(request, 'admission.html', {'form': form})
