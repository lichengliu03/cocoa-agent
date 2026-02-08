#!/usr/bin/env python3
"""
Test script to manually solve the Fed Rate Cut Stock Inflection task.
This validates that the task is solvable and the expected answer is correct.
"""

import numpy as np
from datetime import datetime

# Stock data from the Vercel dashboard (CORRECTED DATA)
# Stock A (NVDA), Stock B (MSFT), Stock C (AMD)
stock_data = {
    'A': {
        'dates': ['2024-08-26', '2024-08-27', '2024-08-28', '2024-08-29', '2024-08-30',
                  '2024-09-03', '2024-09-04', '2024-09-05', '2024-09-06',
                  '2024-09-09', '2024-09-10', '2024-09-11', '2024-09-12',
                  '2024-09-13', '2024-09-16', '2024-09-17', '2024-09-18', '2024-09-19',
                  '2024-09-20', '2024-09-23', '2024-09-24', '2024-09-25', '2024-09-26', '2024-09-27'],
        'prices': [100.0, 100.5, 101.0, 100.8, 101.2,
                   101.5, 101.8, 102.0, 102.2,
                   102.0, 102.5, 103.0, 103.5,
                   104.0, 108.0, 109.0, 108.5, 109.5,
                   110.0, 109.5, 110.5, 110.0, 110.5]
    },
    'B': {
        'dates': ['2024-08-26', '2024-08-27', '2024-08-28', '2024-08-29', '2024-08-30',
                  '2024-09-03', '2024-09-04', '2024-09-05', '2024-09-06',
                  '2024-09-09', '2024-09-10', '2024-09-11', '2024-09-12',
                  '2024-09-13', '2024-09-16', '2024-09-17', '2024-09-18', '2024-09-19',
                  '2024-09-20', '2024-09-23', '2024-09-24', '2024-09-25', '2024-09-26', '2024-09-27'],
        'prices': [400.0, 401.0, 402.0, 403.0, 404.0,
                   405.0, 406.0, 407.0, 408.0,
                   409.0, 410.0, 411.0, 412.0,
                   413.0, 414.0, 415.0, 416.0, 417.0,
                   418.0, 419.0, 420.0, 421.0, 422.0]
    },
    'C': {
        'dates': ['2024-08-26', '2024-08-27', '2024-08-28', '2024-08-29', '2024-08-30',
                  '2024-09-03', '2024-09-04', '2024-09-05', '2024-09-06',
                  '2024-09-09', '2024-09-10', '2024-09-11', '2024-09-12',
                  '2024-09-13', '2024-09-16', '2024-09-17', '2024-09-18', '2024-09-19',
                  '2024-09-20', '2024-09-23', '2024-09-24', '2024-09-25', '2024-09-26', '2024-09-27'],
        'prices': [140.0, 140.5, 141.0, 140.8, 141.2,
                   141.5, 141.8, 142.0, 142.2,
                   142.0, 142.5, 143.0, 143.5,
                   144.0, 149.0, 150.0, 149.5, 150.5,
                   151.0, 150.5, 151.5, 151.0, 151.5]
    }
}

# Fed rate cut date: September 18, 2024
# Analysis window: ±2 trading days = Sept 16-20 (indices 14-18 in extended data)
rate_cut_window = (14, 18)  # Indices for Sept 16-20 in extended data

def calculate_log_returns(prices):
    """Calculate daily log returns."""
    prices_array = np.array(prices)
    log_returns = np.log(prices_array[1:] / prices_array[:-1])
    return log_returns

def check_inflection(log_returns, day_index):
    """
    Check if day_index has an inflection.

    Inflection criterion:
    r(t) > mean(r_{t-10:t-1}) + 2 * std(r_{t-10:t-1})
    """
    if day_index < 10:
        return False, None, None, None

    r_t = log_returns[day_index]
    r_prev = log_returns[day_index-10:day_index]

    mean_prev = np.mean(r_prev)
    std_prev = np.std(r_prev, ddof=1)  # Sample standard deviation

    threshold = mean_prev + 2 * std_prev

    is_inflection = r_t > threshold

    return is_inflection, r_t, threshold, (mean_prev, std_prev)

def analyze_stock(stock_name, data):
    """Analyze a single stock for inflections."""
    prices = data['prices']
    dates = data['dates']

    log_returns = calculate_log_returns(prices)

    print(f"\n{'='*60}")
    print(f"Stock {stock_name}")
    print(f"{'='*60}")

    inflections_in_window = []

    # Check each day in the rate cut window
    # Note: log_returns[i] is the return FROM dates[i] TO dates[i+1]
    # So log_returns[13] is the return on Sept 16 (from Sept 13 to Sept 16)
    for price_idx in range(rate_cut_window[0], rate_cut_window[1] + 1):
        date = dates[price_idx]
        # The log return for this date is at index price_idx - 1
        return_idx = price_idx - 1

        is_inflection, r_t, threshold, stats = check_inflection(log_returns, return_idx)

        if is_inflection:
            mean_prev, std_prev = stats
            print(f"\n✓ INFLECTION on {date}:")
            print(f"  r(t) = {r_t:.6f}")
            print(f"  mean(prev 10) = {mean_prev:.6f}")
            print(f"  std(prev 10) = {std_prev:.6f}")
            print(f"  threshold = {threshold:.6f}")
            inflections_in_window.append((date, r_t, threshold))

    if not inflections_in_window:
        print(f"\n✗ No inflections during Sept 16-20")

    return len(inflections_in_window) > 0

def main():
    print("="*60)
    print("Fed Rate Cut Stock Inflection Analysis")
    print("="*60)
    print("\nTask: Determine how many stocks show price inflection")
    print("      aligned with the Fed rate cut (Sept 18, 2024)")
    print("\nAnalysis window: Sept 16-20, 2024 (±2 trading days)")
    print("\nInflection criterion:")
    print("  r(t) > mean(r_{t-10:t-1}) + 2 × std(r_{t-10:t-1})")

    aligned_stocks = []

    for stock_name, data in stock_data.items():
        is_aligned = analyze_stock(stock_name, data)
        if is_aligned:
            aligned_stocks.append(stock_name)

    print(f"\n{'='*60}")
    print("RESULTS")
    print(f"{'='*60}")
    print(f"\nAligned stocks: {', '.join(aligned_stocks) if aligned_stocks else 'None'}")
    print(f"Count: {len(aligned_stocks)}")
    print(f"\nExpected answer: 2")
    print(f"Calculated answer: {len(aligned_stocks)}")
    print(f"Match: {'✓ PASS' if len(aligned_stocks) == 2 else '✗ FAIL'}")

    return len(aligned_stocks)

if __name__ == "__main__":
    answer = main()
    print(f"\n<answer>{answer}</answer>")
