from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name='customer'


urlpatterns = [
    path('board',views.BoardView.as_view(),name='board_view'),
    path('register',views.RegisterView.as_view(),name='register_view'),
    path('landing',views.LandingView.as_view(),name='landing_view'),
    path('prodreg',views.ProdRegView.as_view(),name = 'prodreg_view')
]

urlpatterns += staticfiles_urlpatterns()
