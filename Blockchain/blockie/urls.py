from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blockie import views

urlpatterns=[
     path('',views.home),
     path('home/light',views.login_page),
     path('home/lol',views.contact_view),
     path('home/about',views.lol),
     path('home/signup',views.register_page)

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()