# Customer Metrics (Python)

This project implements a function that calculates customer-level metrics from order data.

## Overview

You will implement a function that processes order data and returns customer-level aggregated metrics.

## Function to Implement

`get_customer_metrics(data, from_, to, min_total_spend=None)`

This function is located in `metrics.py`.

Your goal is to implement this function so that all tests pass.

## Parameters

- `data`: list of order objects
- `from_`: start date (YYYY-MM-DD, inclusive)
- `to`: end date (YYYY-MM-DD, inclusive)
- `min_total_spend` (optional): minimum total spend per customer

## Requirements

- Date filtering applies to `orderDate` (inclusive)
- Order amount = sum(quantity * unitPrice) across all line items
- Metrics are calculated per customer

Each customer result must include:

- `customerId`
- `orderCount`
- `totalSpend`
- `avgOrderValue`

If `min_total_spend` is provided, only include customers whose totalSpend is greater than or equal to that value.

Results must be sorted by `customerId` ascending.

## Setup

**Install uv** (if not already installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh  # Mac/Linux
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows
```

**Clone and run tests**

```bash
git clone https://github.com/snevans7-commits/customer-metrics-python.git
cd customer-metrics-python
uv run pytest
```

## Important Notes

- Tests may fail initially — this is expected
- Your task is to implement the function so that all tests pass
- You should only modify `metrics.py`

## Do Not

- Do not modify test files
- Do not move or copy files into the `tests/` directory
- Do not rename files or change the project structure
- Do not add configuration files (for example, `conftest.py`) to fix imports

If you are editing anything outside `metrics.py`, you are likely going in the wrong direction.

## Project Structure

    customer-metrics-python
    │
    ├── metrics.py
    ├── pyproject.toml
    ├── README.md
    │
    └── tests
        ├── fixtures.json
        └── test_metrics.py

## Data

Test data is located in:

    tests/fixtures.json
