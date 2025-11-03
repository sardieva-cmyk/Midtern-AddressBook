from django.urls import path
from .views import contact_list, ContactDetailView, ContactCreateView

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('add/', ContactCreateView.as_view(), name='add_contact'),
]