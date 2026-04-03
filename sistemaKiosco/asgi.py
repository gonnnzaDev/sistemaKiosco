import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistemaKiosco.settings')

application = get_asgi_application()



## esto no sirve por el momento pero dejalo igual por las dudas