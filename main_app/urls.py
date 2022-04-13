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
    path('user/<username>', views.profile , name="profile"),
    path('parrotsnacks/', views.parrotsnacks_index, name='parrotsnacks_index'),
    path('parrotsnacks/<int:parrotsnack_id>', views.parrotsnacks_show, name='parrotsnacks_show'),
    path('parrotsnacks/create', views.ParrotSnacksCreate.as_view(), name='parrotsnacks_create'),
    path('parrotsnacks/<int:pk>/update', views.ParrotSnacksUpdate.as_view(), name='parrotsnacks_update'),
    path('parrotsnacks/<int:pk>/delete', views.ParrotSnacksDelete.as_view(), name='parrotsnacks_delete'),
]