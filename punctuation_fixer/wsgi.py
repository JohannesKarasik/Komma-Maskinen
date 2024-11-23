# punctuation_fixer/wsgi.py
"""
WSGI config for punctuation_fixer project.

It exposes the WSGI callable as a module-level variable named `application`.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'punctuation_fixer.settings')

application = get_wsgi_application()