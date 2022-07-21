from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .forms import RegistroForms, FormularioLogin


# Create your views here.

#----USUARIO---#
class RegistroUsuario(CreateView):
    model = User
    template_name = "register.html"
    form_class = RegistroForms
    success_url = reverse_lazy('blog:index')


#----LOGIN---#
class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('blog:index')


    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     return HttpResponseRedirect(self.get_success_url())
        # else:
            return super(Login, self).dispatch(request, *args, **kwargs)



    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)



#----LOGOUT----#
def logoutUser():
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
