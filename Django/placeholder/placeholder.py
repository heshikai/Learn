import hashlib
import os
import sys
from django.conf import settings

DEBUG = os.environ.get('DEBUG','on') == 'on'

print('DEBUG:' + str(DEBUG))

SECRET_KEY = os.environ.get('SECRET_KEY','2poutnm1-hrqu)6e3)xw!(g^z(xpmnw_w#t@(9&^hgnepiy=gk')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS','localhost').split(',')

BASE_DIR = os.path.dirname(__file__)
print('BASE_DIR:' + str(BASE_DIR))
BASE_DIR='/Django/placeholder/'
print(ALLOWED_HOSTS)
print(os.path.join(BASE_DIR,'templates'))
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
    ),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
    ),
    TEMPLATES=(
        {
            'BACKEND':'django.template.backends.django.DjangoTemplates',
            'DIRS':(os.path.join(BASE_DIR,'templates'))
        },
    ),
    STATICFILES_IDR=(
        os.path.join(BASE_DIR,'static')
    ),
    STATIC_URL='/static/'
)

from django.conf.urls import url

from django import forms
from django.http import HttpResponse,HttpResponseBadRequest
from django.shortcuts import render,reverse
from django.views.decorators.http import etag
from django.core.cache import cache
from django.core.wsgi import get_wsgi_application
from io import BytesIO
from PIL import Image,ImageDraw


class ImageForm(forms.Form):
    """FORM to validate requested placeholder image ."""
    height = forms.IntegerField(min_value=1,max_value=2000)
    width  = forms.IntegerField(min_value=1,max_value=2000)

    def generate(self,image_format='PNG'):
        """ Generate am image of the given type and return as raw bytes."""
        height = self.cleaned_data['height']
        width  = self.cleaned_data['width']
        key = '{}.{}.{}'.format(width,height,image_format)
        content = cache.get(key)
        if content is None:
            image = Image.new('RGB',(width,height))
            draw = ImageDraw.Draw(image)
            text = '{} X {}'.format(width,height)
            textwidth,textheight = draw.textsize(text)
            if textwidth < width and textheight < height:
                texttop = (height - textheight) // 2
                textleft = (width - textwidth) // 2
                draw.text((textleft,texttop),text,fill=(255,0,0))
            content=BytesIO()
            image.save(content,image_format)
            content.seek(0)
            cache.set(key,content,60*60)
        return content   

def generate_etag(request,width,height):
    content = 'Placehoder: {0} x {1}'.format(width,height)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()

@etag(generate_etag)    
def placeholder(request,width,height):
    form = ImageForm({'height':height,'width':width})
    if form.is_valid():
        image = form.generate()
        return HttpResponse(image,content_type='image/png')
    else:
        return HttpResponseBadRequest('Inavlid Image Request')

def index(request):
    example = reverse('placeholder',kwargs={'width':50,'height':50})
    context = {
        'example':request.build_absolute_uri(example)
    }
    return render(request,'home.html',context)
#(?P<width>[0-9]+)x(?P<height>[0-9]+)

urlpatterns = [
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)$',placeholder,name='placeholder'),
    url('^$',index,name='homepage')
]

application = get_wsgi_application()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)