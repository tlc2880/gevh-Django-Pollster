"""
# Name: Tommy Cao
# Date: 11/7/17
# Company: GEVH
# Description: Python Django Polling Questionaire.  WSGI config for pollster project.

It exposes the WSGI callable as a module-level variable named ``application``.

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pollster.settings')

application = get_wsgi_application()
