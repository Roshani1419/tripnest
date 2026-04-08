from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Booking, Contact, Brand


def home(request):
    brands = Brand.objects.all()
    return render(request, "index.html", {"brands": brands})


def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect("login")

    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("home")


def packages(request):
    return render(request, "packages.html")


def services(request):
    return render(request, "services.html")


def gallery(request):
    return render(request, "gallery.html")


def about(request):
    return render(request, "about.html")


@login_required(login_url="login")
def book_package(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        package = request.POST.get("package")
        date = request.POST.get("date")

        Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            package=package,
            date=date
        )

        send_mail(
            "New Booking",
            f"{name} booked {package}",
            "admin@gmail.com",
            ["admin@gmail.com"],
            fail_silently=True,
        )

        return render(request, "success.html")

    return render(request, "book.html")


def contact(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return render(request, "contact_success.html")

    return render(request, "contact.html")