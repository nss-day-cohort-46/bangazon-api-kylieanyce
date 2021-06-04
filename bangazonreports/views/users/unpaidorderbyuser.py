"""Module for generating unpaid orders by user report"""
import sqlite3
from django.shortcuts import render
from bangazonreports.views import Connection


def User_unpaidorder_list(request):
    """Function to build an HTML report of unpaid orders by user"""
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT o.id as order_id,
                    u.first_name || ' ' || u.last_name as customer_name,
                    SUM(p.price) invoice_total,
                    u.id user_id
                FROM bangazonapi_order o
                    JOIN bangazonapi_customer c ON c.id = o.customer_id
                    JOIN bangazonapi_orderproduct op ON op.order_id = o.id
                    JOIN bangazonapi_product p ON p.id = op.product_id
                    JOIN auth_user u ON u.id = c.user_id
                WHERE o.payment_type_id IS NULL
                GROUP BY o.id
            """)
            dataset = db_cursor.fetchall()
            unpaidorders_by_user = {}

            for row in dataset:
                unpaidorder = {}
                unpaidorder["customer_name"] = row["customer_name"]
                unpaidorder["order_id"] = row["order_id"]
                unpaidorder["invoice_total"] = row["invoice_total"]

                uid = row["user_id"]
                unpaidorders_by_user[uid] = unpaidorder

            list_of_unpaid_orders = unpaidorders_by_user.values()

            template = 'users/list_of_unpaidorders.html'
            context = {
                'User_unpaidorder_list': list_of_unpaid_orders
            }
            return render(request, template, context)
