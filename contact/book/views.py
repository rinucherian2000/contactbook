
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, UpdateView, DeleteView, CreateView, DetailView
from book.forms import Phoneform
from book.models import Phone
from django.urls import reverse_lazy

# Create your views here.


class AddPhone(CreateView):
    model = Phone
    form_class = Phoneform
    template_name = "phone_add.html"
    success_url = reverse_lazy('listphone')

class PhoneList(ListView):
    model = Phone
    context_object_name = "item"
    template_name = "Listphone.html"

class PhoneDetail(DetailView):
    model = Phone
    context_object_name = "phone"
    template_name = "phone_detail.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listphone')


class Phonedit(UpdateView):
    model = Phone
    form_class = Phoneform
    template_name = "phoneedit.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listphone')


class Phonedelete(DeleteView):
    model = Phone
    template_name = 'phonedelete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("listphone")