"""Module for generating unpaid orders by user report"""
import sqlite3
from django.shortcuts import render
from bangazonapi.models import Order
from bangazonreports.views import Connection


def user_unpaidorder_list(request):
    """Function to build an HTML report of unpaid orders by user"""
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    o.id,
                    c.FirstName || c.LastName as customerName,
                    SUM(total)
                FROM 
                    bangazonapi_order o
                JOIN
                    bangazonapi_customer c ON c.id = o.customerId
                JOIN 
                    bangazonapi_orderProduct op ON op.orderId = o.id
                JOIN
                    bangazonapi_product p ON p.id = op.productId
            """)
