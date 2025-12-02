from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path('add-profile/', views.add_profile, name='add_profile'),  # <-- ADD THIS
    path("recipe/<int:id>/", views.recipe_detail, name="recipe_detail"),
    path("recipe/<int:id>/delete/", views.delete_recipe, name="delete_recipe"),
]
