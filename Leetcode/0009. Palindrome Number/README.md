## [Problem 0007: Reverse Integer](https://leetcode.com/problems/palindrome-number/)

**Difficulty**: Easy

### Problem Description

Given an integer `x`, return `true` if `x` is a palindrome and `false` otherwise.

A palindrome number reads the same backward as forward. Negative numbers are not considered palindromes, as they read differently from left to right and right to left.

### Examples

#### Example 1:
- **Input**: `x = 121`
- **Output**: `true`
- **Explanation**: `121` reads as `121` from left to right and right to left.

#### Example 2:
- **Input**: `x = -121`
- **Output**: `false`
- **Explanation**: From left to right, it reads `-121`. From right to left, it becomes `121-`, hence it’s not a palindrome.

#### Example 3:
- **Input**: `x = 10`
- **Output**: `false`
- **Explanation**: From right to left, it reads `01`, so it’s not a palindrome.

### Constraints

- `-2^31 <= x <= 2^31 - 1`

### Follow-up

Can you solve this problem without converting the integer to a string?

### Performance

- **Runtime**: 10 ms
- **Memory Usage**: 16.7 MB