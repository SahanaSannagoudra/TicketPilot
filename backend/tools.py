
ORDERS = {
    "ORD1001": {
        "order_id": "ORD1001",
        "customer": "Rahul",
        "item": "Wireless Mouse",
        "status": "Shipped",
        "expected_delivery": "2026-11-27"
    },
    "ORD1002": {
        "order_id": "ORD1002",
        "customer": "Priya",
        "item": "Keyboard",
        "status": "Processing",
        "expected_delivery": "2026-11-29"
    },
    "ORD1003": {
        "order_id": "ORD1003",
        "customer": "Arun",
        "item": "Headphones",
        "status": "Delivered",
        "expected_delivery": "Delivered on 2026-11-22"
    }
}


def lookup_order_status(order_id: str) -> dict:

    order = ORDERS.get(order_id.upper())

    if order:
        return order

    return {
        "error": "Order not found",
        "order_id": order_id
    }
