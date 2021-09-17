# Longest-Subsquence-Algorithms

## Dynamic Programming

This repo contains my solution to finding the length of longest sub-sequence such that the difference between the ASCII values of adjacent characters in the subsequence is not more than a given integer K using Dynamic Programming.

Given Question:
Given a string S of length N and an integer K, the task is to find the length of longest sub-sequence such that the difference between the ASCII values of adjacent characters in the subsequence is not more than K.

Examples: 

Input: N = 7, K = 2, S = "afcbedg"
Output: 4
Explanation:
Longest special sequence present 
in "afcbedg" is a, c, b, d.
It is special because |a - c| <= 2, 
|c - b| <= 2 and | b-d| <= 2
