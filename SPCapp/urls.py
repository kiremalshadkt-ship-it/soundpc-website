from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('series/', views.series_list, name='series_list'),
    path('characters/', views.character_list, name='character_list'),
    path('audiobooks/', views.audiobooks, name='audiobooks'),
    path('about/', views.about, name='about'),
    path('audiobooks/black-sun-origins/', views.black_sun_origins, name='black_sun_origins'),
    path('audiobooks/sentinels/', views.sentinels, name='sentinels'),
    path('series/cometson/', views.cometson, name='cometson'),
    path('series/paragons/', views.paragons, name='paragons'),
    path('series/order-of-the-abyss/', views.order_of_the_abyss, name='order_of_the_abyss'),
    path('series/independence-day/', views.independence_day, name='independence_day'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]