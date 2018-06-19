"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""



import os
import codecs


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
#os.environ['LC_ALL']="en_US.UTF-8"

#import os, sys
#if sys.stdout.encoding == None:
 #   os.putenv("PYTHONIOENCODING",'UTF-8')
  #  os.execv(sys.executable,['python']+sys.argv)

application = get_wsgi_application()
