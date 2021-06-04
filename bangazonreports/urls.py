from django.urls import path
from .views import User_unpaidorder_list

urlpatterns = [
    path('reports/unpaidorders', User_unpaidorder_list)
]
