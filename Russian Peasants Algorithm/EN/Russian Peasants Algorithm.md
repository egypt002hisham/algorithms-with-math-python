# Russian Peasants Algorithm Explanation

## Overview

The **Russian Peasants Algorithm** is a method to compute the product of two numbers using halving and doubling operations, combined with binary arithmetic. It maintains an invariant relationship throughout its execution to ensure correctness.

---

## Algorithm Explanation and Proof of Correctness

### Key Steps and Invariant

1. **Initial State**:
   - Start with `x = a`, `y = b`, and `z = 0`.
   - **Invariant**: The product \( a \times b \) is preserved as \( x \times y + z \).  
     Initially: \( a \times b = a \times b + 0 \), so the invariant holds.

2. **Loop Execution**:
   - The loop runs while `x > 0`. In each iteration:
     - If `x` is odd, adjust `z` to maintain the invariant.
     - Halve `x` and double `y` using bitwise operations.

3. **Case 1: `x` is Odd**:
   - **Action**: Add `y` to `z` (`z += y`).  
     This compensates for the remainder when halving an odd `x`.
   - **Update `x` and `y`**:
     - `x` is implicitly decremented by 1 (via `x >> 1` for odd numbers) and halved.
     - `y` is doubled (`y << 1`).

4. **Case 2: `x` is Even**:
   - **Action**: No change to `z`.
   - **Update `x` and `y`**:
     - `x` is halved directly (`x >> 1`).
     - `y` is doubled (`y << 1`).

5. **Maintaining the Invariant**:
   - **Odd Case**:  
     After updating:  
     \( x_{\text{new}} = \frac{x - 1}{2} \), \( y_{\text{new}} = 2y \), \( z_{\text{new}} = z + y \).  
     Substituting into the invariant:  
     \[
     \left(\frac{x - 1}{2}\right) \times 2y + (z + y) = (x - 1)y + z + y = xy + z = a \times b
     \]
   - **Even Case**:  
     After updating:  
     \( x_{\text{new}} = \frac{x}{2} \), \( y_{\text{new}} = 2y \), \( z_{\text{new}} = z \).  
     Substituting into the invariant:  
     \[
     \left(\frac{x}{2}\right) \times 2y + z = xy + z = a \times b
     \]

6. **Termination**:
   - When `x` becomes 0, the invariant simplifies to \( 0 \times y + z = a \times b \).  
   - Thus, `z` contains the final product \( a \times b \).

---

## Code Explanation

### Russian_Peasants_Algorithm(a, b)

This function computes the product of `a` and `b` using the invariant \( a \times b = x \times y + z \).

```python
def Russian_Peasants_Algorithm(a, b):
    x = a  # Initialize x with the first number (a)
    y = b  # Initialize y with the second number (b)
    z = 0  # Initialize z to accumulate the result

    while x > 0:  # Loop until x is reduced to 0
        if x % 2 == 1:  # If x is odd, add y to z to maintain the invariant
            z = y + z

        y = y << 1  # Double y (left shift by 1 bit)
        x = x >> 1  # Halve x (right shift by 1 bit)

    return z  # Return the computed product```

# Explanation of the `binary` Function

The `binary` function demonstrates basic binary operations using bit shifts. Specifically, it divides a number by 2 and multiplies another number by 2, using the right and left shift operations respectively. These operations are commonly used in binary arithmetic for efficient calculations.

## Function Definition

```python
def binary(n, m):
    n = n >> 1  # Divide n by 2 (right shift)
    m = m << 1  # Multiply m by 2 (left shift)
    return n, m  # Return the updated values
```
