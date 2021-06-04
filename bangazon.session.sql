SELECT o.id as order_id,
    u.first_name || u.last_name as customer_name,
    SUM(p.price),
    u.id
FROM bangazonapi_order o
    JOIN bangazonapi_customer c ON c.id = o.customer_id
    JOIN bangazonapi_orderproduct op ON op.order_id = o.id
    JOIN bangazonapi_product p ON p.id = op.product_id
    JOIN auth_user u ON u.id = c.user_id
WHERE o.payment_type_id IS NULL
GROUP BY o.id