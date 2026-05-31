def get_customer_metrics(*, data, from_, to, min_total_spend=None):
    def get_customer_metrics(data, from_, to, min_total_spend=None):
    # Filter orders within the date range
    filtered_orders = [
        order for order in data
        if from_ <= order["orderdate"] <= to
    ]

    # Group orders by customerid and accumulate spend
    customers = {}
    for order in filtered_orders:
        cid = order["customerid"]
        order_total = sum(
            item["quantity"] * item["unitprice"]
            for item in order["items"]
        )
        customers.setdefault(cid, []).append(order_total)

    # Build metrics for each customer
    results = []
    for cid, spends in customers.items():
        ordercount = len(spends)
        totalspend = sum(spends)
        avgordervalue = totalspend / ordercount

        results.append({
            "customerid": cid,
            "ordercount": ordercount,
            "totalspend": totalspend,
            "avgordervalue": avgordervalue
        })

    # Apply minimum spend filter if provided
    if min_total_spend is not None:
        results = [
            r for r in results
            if r["totalspend"] >= min_total_spend
        ]

    # Sort by customerid ascending
    results.sort(key=lambda r: r["customerid"])

    return results

