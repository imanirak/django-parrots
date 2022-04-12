from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"),
    path('parrots/', views.Parrot_List.as_view(), name='parrot_list'),
    path('parrots/new/', views.ParrotCreate.as_view(), name="parrot_create"),
    path('parrots/<int:pk>/', views.Parrot_Detail.as_view(), name="parrot_detail"),
    path('cats/<int:pk>/update', views.Parrot_Update.as_view(), name="parrot_update"),
    path('cats/<int:pk>/delete', views.Parrot_Delete.as_view(), name="parrot_delete"),
    path('user/<username>', views.profile , name="profile")
]