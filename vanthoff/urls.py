from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from landing import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('landing/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('dashboard/', TemplateView.as_view(template_name='dept1.html'), name='home'),
    path('admin/', admin.site.urls),
    path('dell/', include('django.contrib.auth.urls')),
    # path('dept1/', views.compute, name="department1"),
]

