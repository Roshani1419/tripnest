from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    # Home page
    path('', views.home, name="home"),

    #Search bar
    path("search/", views.search_place, name="search"),

    # Login / Register
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("book/", views.book_package, name="book_package"),

    # Packages page
    path('packages/', views.packages, name='packages'),

    # Package details page
    path('package/<str:name>/', views.package_detail, name='package_detail'),

    # Booking
    path('book/', views.book_package, name='book_package'),

    # Services
    path('services/', views.services, name='services'),

    # Gallery
    path('gallery/', views.gallery, name='gallery'),

    # Contact
    path("contact/", views.contact, name="contact"),
    path('contact-success/', views.contact_success, name='contact_success'),

    path('package/<str:name>/', views.package_detail, name='package_detail'),

    #Footer
    path('', views.home, name="home"),

    #Reviews
    path('reviews/', views.reviews, name='reviews'),

    #About us
    path('about/', views.about, name='about'),

]

# MEDIA FILES
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)