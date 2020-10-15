
from django.urls import path, include
from .views import *

urlpatterns = [
    path('ticket/all', TicketListView.as_view()),

    path('executor/<int:pk>', ExecutorRetrieveView.as_view()),
    path('executor/update/<int:pk>', ExecutorUpdateView.as_view()),
    path('executor/all', ExecutorListView.as_view()),
    path('executor/new', ExecutorCreateView.as_view()),

    path('customer/<int:pk>', CustomerRetrieveView.as_view()),
    path('customer/update/<int:pk>', CustomerUpdateView.as_view()),
    path('customer/all', CustomerListView.as_view()),
    path('customer/new', CustomerCreateView.as_view()),


    path('order/<int:pk>', OrderRetrieveView.as_view()),
    path('order/update/<int:pk>', OrderUpdateView.as_view()),
    path('order/all', OrderListView.as_view()),
    path('order/new', OrderCreateView.as_view()),


    path('service/<int:pk>', ServiceRetrieveView.as_view()),
    path('service/update/<int:pk>', ServiceUpdateView.as_view()),
    path('service/all', ServiceListView.as_view()),
    path('service/new', ServiceCreateView.as_view()),

]

