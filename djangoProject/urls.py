from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('comercial',views.comercial,name='comercial'),
    path('hospitalar',views.comercial,name='hospitalar'),
    path('farma',views.comercial,name='farma'),
    path('academiaec',views.academiaec,name='academiaec')

]
