from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

'''
Para visualizar as rotas que estão configuradas no projeto:
from django.urls import get_resolver
from pprint import pprint

pprint(get_resolver().url_patterns[0].urls_patterns)
'''
