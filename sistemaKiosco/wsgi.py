
import os

from django.core.wsgi import get_wsgi_application

##esto es como el app gio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistemaKiosco.settings')

application = get_wsgi_application()
