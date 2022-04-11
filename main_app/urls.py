from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"),
    path('parrots/', views.Parrot_List.as_view(), name='parrot_list'),
    path('user/<username>', views.profile, name="profile")
]