def get_customer_metrics(*, data, from_, to, min_total_spend=None):
from datetime import datetime

def get_customer_metrics(*, data, from_, to, min_total_spend=None):
    start_date = datetime.strptime(from_, "%Y-%m-%d").date()
    end_date = datetime.strptime(to, "%Y-%m-%d").date()

    customers = {}

    for order in data:
        order_date_str = order.get("orderDate", "").split("T")[0]

        try:
            order_date = datetime.strptime(order_date_str, "%Y-%m-%d").date()
        except ValueError:
            continue

        if order_date < start_date or order_date > end_date:
            continue

        customer_id = order.get("customerId")
        if customer_id is None:
            continue

        line_items = order.get("lineItems", [])
        order_amount = sum(
            item.get("quantity", 0) * item.get("unitPrice", 0)
            for item in line_items
        )

        if customer_id not in customers:
            customers[customer_id] = {
                "orderCount": 0,
                "totalSpend": 0
            }

        customers[customer_id]["orderCount"] += 1
        customers[customer_id]["totalSpend"] += order_amount

    results = []

    for customer_id, metrics in customers.items():
        total_spend = metrics["totalSpend"]

        if min_total_spend is not None and total_spend < min_total_spend:
            continue

        order_count = metrics["orderCount"]
        avg_order_value = total_spend / order_count if order_count else 0

        results.append({
            "customerId": customer_id,
            "orderCount": order_count,
            "totalSpend": round(total_spend, 2),
            "avgOrderValue": round(avg_order_value, 2)
        })

    return sorted(results, key=lambda x: x["customerId"])
