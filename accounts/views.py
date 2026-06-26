from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


@method_decorator(ratelimit(key='ip', rate='5/m', method='POST', block=True), name='post')
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'