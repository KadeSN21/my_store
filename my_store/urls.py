from django.contrib import admin
from django.urls import path
from clothes_store.views.home import Index , store
from clothes_store.views.signup import Signup
from clothes_store.views.login import Login , logout
from clothes_store.views.cart import Cart
from clothes_store.views.checkout import CheckOut
from clothes_store.views.orders import OrderView
from clothes_store.middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('admin/', admin.site.urls),


]