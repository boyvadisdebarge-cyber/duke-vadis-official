from django.contrib import admin
from django.urls import path
from website.views import home, booking, contact
urlpatterns=[path("admin/",admin.site.urls),path("",home,name="home"),path("booking/",booking,name="booking"),path("contact/",contact,name="contact")]
