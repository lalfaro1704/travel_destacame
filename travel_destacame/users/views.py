from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from rest_framework import (viewsets, status, parsers, renderers, mixins)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.authtoken.models import Token
from rest_framework.filters import BaseFilterBackend
from rest_framework.authtoken.serializers import AuthTokenSerializer

# my serializers here
from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



















