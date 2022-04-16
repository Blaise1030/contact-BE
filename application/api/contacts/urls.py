from django.urls import path
from . import views


urlpatterns = [
    path('contact/<int:id>', views.contact),
    path('contact', views.createContact),
    path('contacts', views.get_all_contacts)
]
