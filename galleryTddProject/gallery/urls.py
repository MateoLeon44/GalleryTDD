from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/portfolio', views.show_portfolio, name='showPortfolio'),
    path('addUser/', views.add_user_view, name='addUser'),
    path('login/', views.login, name='login'),
    path("edit/", views.edit_user, name="editUser")
]
