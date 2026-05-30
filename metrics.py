def get_customer_metrics(*, data, from_, to, min_total_spend=None):
    # Filter orders within the date range (inclusive)
    filtered_orders = [o for o in data if from_ <= o["orderDate"] <= to]

    # Aggregate metrics per customer
    customers = {}
    for order in filtered_orders:
        cid = order["customerId"]
        line_items = order["lineItems"]

        # Calculate total for this order
        order_amount = sum(
            item["quantity"] * item["unitPrice"]
            for item in line_items
        )

        if cid not in customers:
            customers[cid] = {"orderCount": 0, "totalSpend": 0.0}

        customers[cid]["orderCount"] += 1
        customers[cid]["totalSpend"] += order_amount

    # Build results, sorted by customerId ascending
    result = []
    for cid in sorted(customers):
        m = customers[cid]
        if min_total_spend is not None and m["totalSpend"] < min_total_spend:
            continue
        result.append({
            "customerId": cid,
            "orderCount": m["orderCount"],
            "totalSpend": m["totalSpend"],
            "avgOrderValue": m["totalSpend"] / m["orderCount"],
        })

    return result
