SELECT o.id as order_id,
    u.first_name || u.last_name as customer_name
FROM bangazonapi_order o
    JOIN bangazonapi_customer c ON c.id = o.customer_id
    JOIN bangazonapi_orderproduct op ON op.order_id = o.id
    JOIN bangazonapi_product p ON p.id = op.product_id
    JOIN auth_user u ON u.id = c.user_id