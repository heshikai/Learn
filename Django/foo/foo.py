

import os
import sys
from django.conf import settings

DEBUG = os.environ.get('DEBUG','on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY','$b@a^kif%%%9*45td&2feb8nj=zuh5f(lkov6)xa1v_58)g&=n')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS','localhost').split(',')

print(ALLOWED_HOSTS)

settings.configure(
    DEBUG=DEBUG,
    #SECRET_KEY='thisisthesecretkey',
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS = ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfviewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
)

from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application



def index(request):
    return HttpResponse("Hello,World!2018-12-24")


urlpatterns = {
    url('^$',index)
}

application = get_wsgi_application()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)