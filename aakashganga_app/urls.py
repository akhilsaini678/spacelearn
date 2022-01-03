from django.urls import path
from . import views

urlpatterns = [
    path('',views.fun_index,name='index'),
    path('sun/',views.fun_sun,name='sun'),
    path('mercury/',views.fun_mercury,name='mercury'),
    path('venus/',views.fun_venus,name='venus'),
    path('earth/',views.fun_earth,name='earth'),
    path('mars/',views.fun_mars,name='mars'),
    path('jupiter/',views.fun_jupiter,name='jupiter'),
    path('saturn/',views.fun_saturn,name='saturn'),
    path('uranus/',views.fun_uranus,name='uranus'),
    path('neptune/',views.fun_neptune,name='neptune'),
    path('pluto/',views.fun_pluto,name='pluto'),
    path('milkyway/',views.fun_milkyway,name='milkyway'),
    path('andromeda/',views.fun_andromeda,name='andromeda'),
    path('contact/',views.fun_contact,name='contact'),
    path('login/',views.fun_login,name='login'),
    path('register/',views.fun_register,name='register'),
    path('questions/',views.fun_questions,name='questions'),
]
