from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Booking, Contact, Brand


# ---------------- HOME ----------------
def home(request):
    brands = Brand.objects.all()
    return render(request, "index.html", {"brands": brands})


# ---------------- AUTH ----------------
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
        else:
            return render(request, "login.html",
                          {"error": "Invalid username or password"})

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("home")


# ---------------- PAGES ----------------
def packages(request):
    return render(request, "packages.html")


def services(request):
    return render(request, "services.html")


def gallery(request):
    return render(request, "gallery.html")


def about(request):
    return render(request, "about.html")


def reviews(request):
    return render(request, "reviews.html")


# ---------------- BOOKING ----------------
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
            "New Tour Booking",
            f"""
New Booking Received 

Name: {name}
Email: {email}
Phone: {phone}
Package: {package}
Date: {date}
""",
            "roshanirangrej4@gmail.com",
            ["roshanirangrej@gmail.com"],
            fail_silently=False,
        )
    except Expection as e:
         print (e)
    
    messages.success(request, "Booking Successful")


    return render(request, "book.html")


# ---------------- CONTACT ----------------
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

        send_mail(
            subject,
            message,
            email,
            ["your_email@gmail.com"],
            fail_silently=True,
        )

        return render(request, "contact_success.html")

    return render(request, "contact.html")


# ---------------- PACKAGE DETAIL ----------------
def package_detail(request, name):

    packages = {
        "Ladakh": {"duration": "5 Days", "price": "₹30,000"},
        "Lakshwadeep": {"duration": "5 Days", "price": "₹35,000"},
        "Rajasthan": {"duration": "6 Days", "price": "₹25,000"},
        "Rameshwaram": {"duration": "5 Days", "price": "₹20,000"},
    }

    package = packages.get(name)

    return render(request, "package_detail.html",
                  {"package": package, "name": name})


# ---------------- SEARCH ----------------
def search_place(request):

    if request.method == "GET":

        query = request.GET.get("q")

        if query:
            query = query.lower()

            if query == "ladakh":
                return redirect("package_detail", name="Ladakh")

            elif query == "lakshwadeep":
                return redirect("package_detail", name="Lakshwadeep")

            elif query == "rajasthan":
                return redirect("package_detail", name="Rajasthan")

            elif query == "rameshwaram":
                return redirect("package_detail", name="Rameshwaram")

    return redirect("home")