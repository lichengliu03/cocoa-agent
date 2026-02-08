#!/usr/bin/env python3
"""
Generate realistic stock data that produces exactly 2 inflections
during the Fed rate cut window (Sept 16-20, 2024).

Stock A (NVDA): Inflection on Sept 16
Stock B (MSFT): No inflection
Stock C (AMD): Inflection on Sept 16

Expected answer: 2
"""

import numpy as np
import json

# Stock A (NVDA) - designed to have inflection on Sept 16
prices_a = [
    # Aug 26-30: Gradual decline
    100.00, 100.50, 101.00, 100.80, 101.20,
    # Sept 3-6: Continued gradual movement
    101.50, 101.80, 102.00, 102.20,
    # Sept 9-13: Steady small gains
    102.00, 102.50, 103.00, 103.50,
    # Sept 13-20: Sept 16 has significant jump (inflection!)
    104.00, 108.00, 109.00, 108.50, 109.50,
    # Sept 20-27: Continued movement
    110.00, 109.50, 110.50, 110.00, 110.50
]

# Stock B (MSFT) - designed to have NO inflection
prices_b = [
    # Aug 26-30: Steady gradual increase
    400.00, 401.00, 402.00, 403.00, 404.00,
    # Sept 3-6: Continued steady increase
    405.00, 406.00, 407.00, 408.00,
    # Sept 9-13: Steady increase continues
    409.00, 410.00, 411.00, 412.00,
    # Sept 13-20: No significant jump, just steady movement
    413.00, 414.00, 415.00, 416.00, 417.00,
    # Sept 20-27: Continued steady movement
    418.00, 419.00, 420.00, 421.00, 422.00
]

# Stock C (AMD) - designed to have inflection on Sept 16
prices_c = [
    # Aug 26-30: Gradual movement
    140.00, 140.50, 141.00, 140.80, 141.20,
    # Sept 3-6: Small fluctuations
    141.50, 141.80, 142.00, 142.20,
    # Sept 9-13: Steady small gains
    142.00, 142.50, 143.00, 143.50,
    # Sept 13-20: Sept 16 has significant jump (inflection!)
    144.00, 149.00, 150.00, 149.50, 150.50,
    # Sept 20-27: Continued movement
    151.00, 150.50, 151.50, 151.00, 151.50
]

dates = [
    '2024-08-26', '2024-08-27', '2024-08-28', '2024-08-29', '2024-08-30',
    '2024-09-03', '2024-09-04', '2024-09-05', '2024-09-06',
    '2024-09-09', '2024-09-10', '2024-09-11', '2024-09-12',
    '2024-09-13', '2024-09-16', '2024-09-17', '2024-09-18', '2024-09-19',
    '2024-09-20', '2024-09-23', '2024-09-24', '2024-09-25', '2024-09-26', '2024-09-27'
]

# Verify inflections
def check_inflection(prices, date_idx):
    log_returns = np.log(np.array(prices[1:]) / np.array(prices[:-1]))
    return_idx = date_idx - 1

    if return_idx < 10:
        return False, None, None

    r_t = log_returns[return_idx]
    r_prev = log_returns[return_idx-10:return_idx]
    mean_prev = np.mean(r_prev)
    std_prev = np.std(r_prev, ddof=1)
    threshold = mean_prev + 2 * std_prev

    return r_t > threshold, r_t, threshold

print("Verification:")
print("="*60)

for stock_name, prices in [('A (NVDA)', prices_a), ('B (MSFT)', prices_b), ('C (AMD)', prices_c)]:
    print(f"\nStock {stock_name}:")
    # Check Sept 16 (index 14)
    has_inflection, r_t, threshold = check_inflection(prices, 14)
    if r_t is not None:
        print(f"  Sept 16: r(t)={r_t:.6f}, threshold={threshold:.6f}")
        print(f"  Inflection: {has_inflection}")

print("\n" + "="*60)
print("Expected answer: 2 (Stock A and Stock C)")
print("="*60)

# Output JavaScript format for index.html
print("\n\nJavaScript data for index.html:")
print("="*60)

stock_data = {
    'A': {'dates': dates, 'prices': prices_a},
    'B': {'dates': dates, 'prices': prices_b},
    'C': {'dates': dates, 'prices': prices_c}
}

print(json.dumps(stock_data, indent=4))
