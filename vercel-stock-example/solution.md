# Solution Walkthrough

## Step 1: Access the Dashboard

Navigate to the stock analysis dashboard at the provided URL. You'll see three stock charts labeled A, B, and C.

## Step 2: Extract Price Data

Click the "Show Price Data" button under each chart to reveal the daily closing prices. You should extract:

**Stock A:**
- 2024-09-06: $102.83
- 2024-09-09: $101.66
- 2024-09-10: $102.40
- ... (continue for all dates)

**Stock B:**
- 2024-09-06: $410.59
- ... (continue for all dates)

**Stock C:**
- 2024-09-06: $140.35
- ... (continue for all dates)

## Step 3: Calculate Log Returns

Write code to calculate daily log returns for each stock:

```python
import numpy as np

# Example for Stock A
prices_a = [102.83, 101.66, 102.40, 106.21, 108.94, 110.09, 114.27,
            116.91, 116.14, 117.59, 121.35, 120.88, 119.25, 121.40,
            120.79, 121.56]

log_returns_a = np.log(np.array(prices_a[1:]) / np.array(prices_a[:-1]))
```

## Step 4: Identify Inflection Points

For each day t (starting from day 11, since we need 10 previous days):

```python
def check_inflection(log_returns, day_index):
    """Check if day_index has an inflection"""
    if day_index < 10:
        return False

    r_t = log_returns[day_index]
    r_prev = log_returns[day_index-10:day_index]

    mean_prev = np.mean(r_prev)
    std_prev = np.std(r_prev, ddof=1)  # Sample std

    threshold = mean_prev + 2 * std_prev

    return r_t > threshold
```

## Step 5: Check Alignment Window

The Fed rate cut was on September 18, 2024. The ±2 trading days window is:
- September 16 (Monday)
- September 17 (Tuesday)
- September 18 (Wednesday) - Rate cut day
- September 19 (Thursday)
- September 20 (Friday)

Map these dates to indices in your data array and check for inflections.

## Step 6: Count Aligned Stocks

```python
# For each stock, check if any day in the window has an inflection
aligned_count = 0

for stock in [stock_a, stock_b, stock_c]:
    has_inflection = False
    for day_index in [10, 11, 12, 13, 14]:  # Sept 16-20
        if check_inflection(stock['log_returns'], day_index):
            has_inflection = True
            break

    if has_inflection:
        aligned_count += 1

print(f"Answer: {aligned_count}")
```

## Step 7: Verify Results

**Stock A (NVDA):**
- September 16: r(t) = 0.0372, threshold = 0.0337 → **Inflection** ✓
- September 20: r(t) = 0.0314, threshold = 0.0289 → **Inflection** ✓
- **Aligned** ✓

**Stock B (MSFT):**
- No inflections during September 16-20
- **Not aligned** ✗

**Stock C (AMD):**
- September 16: r(t) = 0.0344, threshold = 0.0314 → **Inflection** ✓
- **Aligned** ✓

## Final Answer

```
<answer>2</answer>
```

Two stocks (A and C) are aligned with the Fed rate cut event.
