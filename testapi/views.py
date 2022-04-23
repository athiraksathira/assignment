from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import CreateView, ListView

from testapi.forms import UserForm
from testapi.models import UserModel
from django.urls import reverse_lazy



class AddUser(CreateView):
    model=UserModel
    form_class=UserForm
    template_name="adduser.html"
    success_url=reverse_lazy ("listuser")
class ListUser(ListView):
    model = UserModel
    template_name = "listuser.html"
    context_object_name = "users"
class DeleteUser(View):
    def get(self, request, *args, **kwargs):
        qs = UserModel.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("listuser")

