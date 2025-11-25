"""
ASGI config for P2_S7_Fase_4_Proyecto_Integrador_Grupo3_202610 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'P2_S7_Fase_4_Proyecto_Integrador_Grupo3_202610.settings')

application = get_asgi_application()
