# 🏠 House Robber - LeetCode (Medium)

## 📘 Problem

This repository contains my Python solution to the **"House Robber"** problem from LeetCode.

- **Difficulty:** Medium  
- **Topic:** 1D Dynamic Programming  
- **Language:** Python  
- **LeetCode Link:** [House Robber](https://leetcode.com/problems/house-robber/)

### Problem Summary:
You are a professional robber planning to rob houses along a street, but you can't rob two adjacent houses.  
The goal is to calculate the maximum amount of money you can rob without triggering alarms.

---

## 🧠 Approach

This solution is implemented using a **recursive backtracking** technique:

- At each step, we choose to rob a house and skip the next one (i.e., jump ahead by 2).
- All combinations are explored, and the maximum sum is returned.
- Results are stored in a list and the highest value is taken as the answer.

> ⚠️ This solution is **not optimized** for large inputs. It is designed for understanding the structure of the problem.
