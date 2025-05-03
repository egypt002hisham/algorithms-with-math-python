# Russian Peasants Algorithm Explanation

## The Algorithm in Simple Terms

- A smart way to multiply two numbers **without directly using multiplication**, by:
  1. **Continuously halving the first number (x)** (until it becomes zero).
  2. **Doubling the second number (y)** in each step.
  3. **Adding values of (y)** in specific cases to get the final result.

---

## How the Algorithm Works Step by Step

### Variables Used:

- `x`: The first number (which is halved in each step).
- `y`: The second number (which is doubled in each step).
- `z`: The place where the final result is stored.

### Execution Steps:

1. **Start with**:

   - `x = first number` (e.g., 5)
   - `y = second number` (e.g., 4)
   - `z = 0`

2. **Repeat the following until `x = 0`**:

   - **If `x` is odd**:
     - Add the value of `y` to `z`.
     - Decrease `x` by 1 (to make it even).
   - **Divide `x` by 2** and **double `y`**.

3. **When `x = 0`**, `z` will hold the multiplication result.

---

## Practical Example (5 × 4):

| Step | x   | y   | z   | Explanation                    |
| ---- | --- | --- | --- | ------------------------------ |
| 1    | 5   | 4   | 0   | `x` is odd → Add 4 to `z`      |
| 2    | 2   | 8   | 4   | `x` is even → No change in `z` |
| 3    | 1   | 16  | 4   | `x` is odd → Add 16 to `z`     |
| 4    | 0   | 32  | 20  | Stop → Final result `z = 20`   |

**Note**:

- In the first step: Since `x = 5` (odd), we added `y = 4` to `z`.
- In the last step: When `x = 0`, the loop stops, and `z = 20` (which is 5 × 4).

---

## Why Does This Algorithm Work? 🧐

- **The Core Idea**:

  - Every time we **halve `x`** (÷2) and **double `y`** (×2), the product `x * y` remains the same.  
    Example:  
    `x = 4`, `y = 4` → `4*4 = 16`  
    After halving/doubling: `x = 2`, `y = 8` → `2*8 = 16`

- **Odd `x` Case**:
  - When halving an odd number, we subtract 1 first to make it even.  
    Example: `5 ÷ 2 = 2.5`, but in the algorithm:  
    `(5 - 1) ÷ 2 = 2` (we ignore the decimal).
    - The remainder (1) represents the value of `y` added to `z`.

---

## Python Code

```python
def multiply(a, b):
    x = a  # First number (to be halved)
    y = b  # Second number (to be doubled)
    z = 0  # Final result

    while x > 0:
        if x % 2 == 1:    # If x is odd
            z += y        # Add y to z

        x = x // 2        # Halve x (ignore decimals)
        y = y * 2         # Double y

    return z              # Final result

print(multiply(5, 4))     # 20

```

# Explanation of the `binary` Function

The `binary` function demonstrates basic binary operations using bit shifts. Specifically, it divides a number by 2 and multiplies another number by 2, using the right and left shift operations respectively. These operations are commonly used in binary arithmetic for efficient calculations.

## Function Definition

```python
def binary(n, m):
    n = n >> 1  # Divide n by 2 (right shift)
    m = m << 1  # Multiply m by 2 (left shift)
    return n, m  # Return the updated values
```

# Multiply and Divide use binary

```python
def multiply(a, b):
    x = a  # First number (to be halved)
    y = b  # Second number (to be doubled)
    z = 0  # Final result

    while x > 0:
        if x % 2 == 1:    # If x is odd
            z += y        # Add y to z

        x = x << 1       # Halve x using binary shift (left shift)
        y = y >> 1       # Double y using binary shift (right shift)

    return z              # Final result

print(multiply(5, 4))     # 20

```
