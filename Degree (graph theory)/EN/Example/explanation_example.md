# 📚 Simple Multiplication Algorithm Using Graph Theory

## 🧠 Concept

This algorithm performs multiplication using only addition and a loop, based on **graph theory representation**.  
It treats values as **nodes**, and operations as **edges** between them.

---

## 🧮 Code with Graph Theory Comments

```python
def start(a, b):
    # Node z: represents the product of multiplication, initially 0 (receiving node)
    z = 0

    # Loop continues as long as the degree of node a > 0 (number of repetitions = initial a)
    while a > 0:
        # 1️⃣ Add value b to z: an edge from node a to z via fixed value b
        z = z + b  # z += b

        # 2️⃣ Decrease the degree of node a by 1: simulating a self-loop being removed
        a = a - 1  # degree of a = remaining repetitions

    return z  # Return final value of node z

r = start(2, 2)
print(r)  # Output: 4

[a: degree=2] ───► [b: value=2] ───► [z: value=0]
  │
  ▼  (loop subtracts 1 from a's degree every iteration)
[a: degree=1] ───► [b: value=2] ───► [z: value=2]
  │
  ▼
[a: degree=0] ───► [b: value=2] ───► [z: value=4]
```
