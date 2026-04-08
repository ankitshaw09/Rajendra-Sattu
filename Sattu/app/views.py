from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib import messages
import random


# Create your views here.


def home(request):
    return render(request, "index.html")


def products(request):
    return render(request, "product.html")


def story(request):
    return render(request, "story.html")


from django.core.mail import EmailMessage
from django.conf import settings


def contact(request):
    if request.method == "POST":
        user_captcha = request.POST.get("captcha")
        real_captcha = request.session.get("captcha")
        if not user_captcha or user_captcha != real_captcha:
            messages.error(request, "Invalid captcha!")
            return redirect("contact")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save to DB
        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        # 📩 1. Email to OWNER
        owner_email = EmailMessage(
            subject=f"New Inquiry: {subject}",
            body=f"""
Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
""",
            from_email=settings.EMAIL_HOST_USER,
            to=["ankitshaw.py@gmail.com"],
            reply_to=[email],
        )
        owner_email.send()

        # 📩 2. Email to USER (confirmation)
        user_email = EmailMessage(
            subject="We received your inquiry ✅",
            body=f"""
Hi {name},

Thank you for contacting Rajendra Sattu.

We have received your message:
"{message}"

Our team will contact you soon.

Regards,
Rajendra Sattu Team
""",
            from_email=settings.EMAIL_HOST_USER,
            to=[email],  # 🔥 send to user
        )
        user_email.send()
        
        request.session.pop("captcha", None)
        messages.success(request, "Message sent successfully!")
        return redirect("contact")
    
    captcha = str(random.randint(1000, 9999))
    request.session["captcha"] = captcha
    

    return render(request, "contact.html", {"captcha": captcha})


def process(request):
    return render(request, "ourProcess.html")
