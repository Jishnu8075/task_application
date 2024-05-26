from django.shortcuts import render,redirect
from django.views.generic import *
from django.urls import reverse_lazy,reverse
from django.contrib import messages

from task.models import *
from task.forms import *


# Create your views here.
class RegistrationView(CreateView):
    template_name="signup.html"
    form_class=RegistrationForm
    model=User
    success_url=reverse_lazy("login")

    def form_valid(self,form):
        messages.success(self.request,"account created")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,"failed")
        return super().form_invalid(form)


class LoginView(FormView):
    template_name="login.html"
    form_class=LoginForm
    success_url=reverse_lazy("task-add")

class TaskAddView(CreateView,ListView):
    template_name="task_add.html"
    model=Task
    context_object_name="task"
    form_class=TaskAddForm
    success_url=reverse_lazy('task-list')

    def form_valid(self,form):
        messages.success(self.request,("succesfully added"))
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,("failed"))
        return super().form_invalid(form)

class TaskListView(ListView):
    template_name="task_list.html"
    model=Task
    context_object_name="tasks"

class DeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Task.objects.get(id=id).delete()
        return redirect(reverse("task-add"))
    
class UpdateTaskView(UpdateView):
    template_name="update.html"
    model=Task
    form_class=TaskAddForm
    success_url=reverse_lazy("task-list")

class DetailTaskView(DetailView):
    template_name='detail.html'
    model=Task
    context_object_name="task"
    