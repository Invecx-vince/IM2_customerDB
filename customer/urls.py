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
    path('prodreg',views.ProdRegView.as_view(),name = 'prodreg_view'),
    path('products',views.ProductView.as_view(),name='products_view'),
    path('cart',views.CartView.as_view(),name='cart_view')
]

urlpatterns += staticfiles_urlpatterns()
