from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django_hosts.resolvers import reverse
from django.views.defaults import bad_request, permission_denied, page_not_found, server_error
import random

from vulnexamples.views import HostsLoginView, HostsRegistrationView


def index(request):
    return render(request, 'a9_cve/index.html')


class RegistrationView(HostsRegistrationView):
    subdomain = 'a9_cve'


class LoginView(HostsLoginView):
    subdomain = 'a9_cve'


def logout_view(request):
    logout(request)
    return redirect(reverse('index', host='a9_cve'))
