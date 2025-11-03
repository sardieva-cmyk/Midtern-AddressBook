from django.shortcuts import render
from django.views.generic import DetailView,
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Contact

def contact_list(request):
    contacts = Contact.objects.all().order_by('last_name')
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contacts/contact_detail.html'
    context_object_name = 'contact'

class ContactCreateView(CreateView):
    model = Contact
    fields = ['last_name', 'first_name', 'middle_name', 'phone', 'email', 'photo', 'birth_date']
    template_name = 'contacts/contact_form.html'
    success_url = reverse_lazy('contact_list')