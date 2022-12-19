from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('articles/',include('articles.urls')),
    path('admin/', admin.site.urls),
    path('about/',views.about),
    path('',views.homepage),
]

urlpatterns+=staticfiles_urlpatterns()