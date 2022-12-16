from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from clothes_store.models.customer import Customer
from django.views import View
from clothes_store.models.productio import Products
from clothes_store.models.orders import Order
from clothes_store.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})