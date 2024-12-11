# Chess Champions

This repository contains a Python solution to the chess champions coding challenge. The challenge involves identifying "champion" chess players from a list based on specific criteria.

## Problem Statement

A player is considered a "champion" if:
1. No other player is both **strictly younger** and has the **same or higher score**.
2. No other player is both **strictly stronger** and of the **same or younger age**.

The goal is to implement a function that extracts all champions from a given list of players efficiently and accurately.

---

## Solution Overview

The solution is implemented in `find_champions.py` and consists of:
1. **Sorting** the list of players by age (ascending) and score (descending).
2. **Single traversal** of the sorted list to determine champions based on conditions:
   - A player is considered a champion if their score is greater than the maximum score seen so far.
   - Players with the same score and age are grouped together and considered champions.

---

## Complexity Analysis

1. **Sorting Step**:
   - Sorting players by age and score has a complexity of \(O(n \log n)\), where \(n\) is the number of players.
2. **Single Traversal**:
   - The loop to determine champions runs in \(O(n)\).
   
Overall, the algorithm has a time complexity of \(O(n \log n)\), dominated by the sorting step, and a space complexity of \(O(n)\) due to the storage of the `champions` list.

---

## Step-by-Step Logic

1. **Handle Empty Input**:  
   If the input list of players is empty, the function returns an empty list immediately.
   
2. **Sorting**:  
   Players are sorted by:
   - Age in ascending order.
   - Score in descending order (to prioritize stronger players of the same age).

3. **Iterate Through Players**:  
   - For each player, check if they have a higher score than the current maximum score seen so far.  
   - If two players have the same age and score, they are both considered champions.

4. **Update Score and Age Tracking**:  
   - After processing each player, update the maximum score and the current age group.

5. **Return Champions**:  
   The list of champions is returned as the result.

---

## Edge Cases Considered

1. **Empty List**:  
   - Input: `[]`  
   - Output: `[]`
   
2. **Single Player**:  
   - Input: `[("Alice", 30, 2400)]`  
   - Output: `[("Alice", 30, 2400)]`
   
3. **Players with Identical Age and Score**:  
   - Input: `[("Alice", 28, 2400), ("Bob", 28, 2400)]`  
   - Output: `[("Alice", 28, 2400), ("Bob", 28, 2400)]`
   

---

## Example Usage

```python
from find_champions import find_champions

players = [
    ("Alice", 30, 2400),
    ("Bob", 28, 2500),
    ("Charlie", 32, 2300),
    ("Diana", 28, 2500),  # Same age and score
]

champions = find_champions(players)
if not champions:
    print("Pas de champions trouvés.")
else:
    print("Les champions sont :", champions)

