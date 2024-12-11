# Chess Champions

This repository contains a Python solution to the chess champions coding challenge. The challenge involves identifying "champion" chess players from a list based on specific criteria.

## Problem Statement

A player is considered a "champion" if:
1. No other player is both **strictly younger** and has the **same or *higher score**.
2. No other player is both **strictly stronger** and of the **same or younger age**.

The goal is to implement a function that extracts all champions from a given list of players efficiently and accurately.

## Solution

The solution is implemented in `find_champions.py`. It uses:
- Sorting by age (ascending) and score (descending).
- A linear pass to identify champions based on the highest scores seen so far.

### Example Input and Output
```python
players = [
    ("Alice", 30, 2400),
    ("Bob", 28, 2500),
    ("Charlie", 32, 2300),
]

# Output: [("Bob", 28, 2500), ("Alice", 30, 2400)]
