from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Booking, Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



def home(request):
    return render(request, 'index.html')


def login_user(request):
    return render(request, 'login.html')


def register_user(request):
    return render(request, 'register.html')


def logout_user(request):
    return render(request, 'index.html')


def packages(request):
    return render(request, 'packages.html')


@login_required(login_url='login')
def book_package(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        package = request.POST.get('package')
        date = request.POST.get('date')

        Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            package=package,
            date=date
        )

        return redirect('index')
    
    return render(request, 'book.html')

        # Send email to admin
        send_mail(
            "New Tour Booking",
            "New booking from {name}\nEmail: {email}\nPhone: {phone}\nPackage: {package}\nDate: {date}",
            "roshanirangrej4@gmail.com",
            ["roshanirangrej4@gmail.com"],
            fail_silently=False,
        )

        return render(request, "success.html")

    # THIS LINE IS IMPORTANT
    return render(request, "book.html")

def services(request):

    services = [

        {
            "title": "Affordable Hotels",
            "icon": "🏨",
            "description": "Book comfortable and budget friendly hotels for your trip."
        },

        {
            "title": "Fast Travel",
            "icon": "✈️",
            "description": "Quick and safe travel arrangements to reach your destination."
        },

        {
            "title": "Food & Drinks",
            "icon": "🍽️",
            "description": "Enjoy delicious local food and refreshing drinks."
        },

        {
            "title": "Adventures",
            "icon": "🏔️",
            "description": "Experience trekking, rafting and thrilling adventure activities."
        },

        {
            "title": "24/7 Support",
            "icon": "📞",
            "description": "Our support team is available anytime to help you."
        }

    ]

    return render(request, "services.html", {"services": services})



def gallery(request):
    return render(request,"gallery.html")

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save message to database
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Send email to admin
        send_mail(
            subject,
            message,
            email,
            ["roshanirangrej4@gmail.com"],
            fail_silently=True,
        )

        return render(request, "contact_success.html")

    return render(request, "contact.html")

from .models import Brand

def home(request):
    brands = Brand.objects.all()  # fetch all brand logos
    return render(request, "index.html", {"brands": brands})


def home(request):
    # Add logos for trusted brands
    brands = [
        {"name": "Brand 1", "logo": "images/brand1.jpeg"},
        {"name": "Brand 2", "logo": "images/brand2.jpeg"},
        {"name": "Brand 3", "logo": "images/brand3.jpeg"},
        {"name": "Brand 4", "logo": "images/brand4.jpeg"},
        {"name": "Brand 5", "logo": "images/brand5.jpeg"},
    ]
    return render(request, 'index.html', {"brands": brands})


def package_detail(request, name):

    packages = {

        "Ladakh": {
            "duration": "5 Days / 4 Nights",
            "price": "₹30,000",
            "itinerary": [
                "Day 1: Arrival in Leh & acclimatization.",
                "Day 2: Thiksey Monastery, Hemis Monastery & Leh Palace.",
                "Day 3: Pangong Lake excursion.",
                "Day 4: Nubra Valley – camel safari & Diskit Monastery.",
                "Day 5: Magnetic Hill, Shanti Stupa & departure."
            ]
        },

        "Lakshwadeep": {
            "duration": "5 Days / 4 Nights",
            "price": "₹35,000",
            "itinerary": [
                "Day 1: Arrival at Agatti island-beach relaxtion.",
                "Day 2: Snorkeling & scuba diving at Agatti reefs.",
                "Day 3: Island hopping – Bangaram & Kadmat.",
                "Day 4: Kayaking & beach games – visit Kavaratti.",
                "Day 5: Sunrise view & Departure."
            ]
        },

        "Rajasthan": {
            "duration": "6 Days / 5 Nights",
            "price": "₹25,000",
            "itinerary": [
                "Day 1: Arrival in Jaipur – City Palace & Hawa Mahal.",
                "Day 2: Visit Amber Fort & Jantar Mantar.",
                "Day 3: Travel to Jodhpur – Mehrangarh Fort & Clock Tower.",
                "Day 4: Udaipur – City Palace & Lake Pichola boat ride.",
                "Day 5: Kumbhalgarh Fort & local village visit",
                "Day 6: Departure."
            ]
        },

         "Rameshwaram": {
            "duration": "5 Days / 4 Nights",
            "price": "₹20,000",
            "itinerary": [
                "Day 1: Arrival – Ramanathaswamy Temple & Agnitheertham.",
                "Day 2: Dhanushkodi Beach & Pamban Bridge.",
                "Day 3: Ramar Patham & Kothandaramaswamy Temple.",
                "Day 4: Local markets, beach relaxation & sightseeing.",
                "Day 5: Temple visit & departure."
            ]
        },
        
    }


    package = packages.get(name)

    return render(request, "package_detail.html", {
        "package": package,
        "name": name
    })

def search_place(request):

    if request.method == "GET":

        query = request.GET.get("q")

        if query:
            query = query.lower()

            if query == "ladakh":
                return redirect("package_detail", name="Ladakh")

            elif query == "lakshwadeep":
                return redirect("package_detail", name="Lakshwadeep")

            elif query == "rajsthan":
                return redirect("package_detail", name="Rajsthan")

            elif query == "rameshwaram":
                return redirect("package_detail", name="Rameshwaram")

    return redirect("home")

def register_user(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        return redirect("login")

    return render(request, "register.html")

def login_user(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            return render(request, "login.html", {"error":"Invalid username or password"})

    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect("home")

from django.shortcuts import render

def home(request):
    return render(request, "index.html")   # Home page

def reviews(request):
    return render(request, "reviews.html") # Reviews page

def about(request):
    return render(request, "about.html")
    

from django.shortcuts import render
from .models import Brand

def home(request):
    brands = Brand.objects.all()
    return render(request, "index.html", {"brands": brands})