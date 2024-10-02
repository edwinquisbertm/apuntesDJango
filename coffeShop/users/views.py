from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy(
        "login"
    )  # reverse_lazy es para redirigir a una url despues de que se haya completado el registro
