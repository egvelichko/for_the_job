"""System module."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """"app registration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
