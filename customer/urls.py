from django.urls import path
from . import views

app_name='customer'


urlpatterns = [
    path('board',views.BoardView.as_view(),name='board_view'),
    path('register',views.RegisterView.as_view(),name='register_view'),
    path('landing',views.LandingView.as_view(),name='landing_view')
]