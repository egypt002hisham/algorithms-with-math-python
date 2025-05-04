# مقارنة بين طريقة الضرب التقليدية وخوارزمية الفلاح الروسي (Russian Peasant Multiplication)

## 🇦🇪 النسخة العربية

### ✅ الطريقة التقليدية (Naive Multiplication)

```python
def naive(a, b):
    z = 0
    while a > 0:
        z = z + b
        a = a - 1
    return z
```

- الفكرة: جمع b عدد a من المرات.
- الزمن: كل تكرار يحتوي على عمليتين (جمع وإنقاص).
- عدد التكرارات = a → الزمن = **O(a)**

### ✅ خوارزمية الفلاح الروسي (Russian Peasant)

```python
def russian(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z = z + y
        x = x // 2
        y = y * 2
    return z
```

- الفكرة: نقسم `a` على 2 كل مرة، ونضاعف `b`، ونضيف `b` إلى الناتج إذا كانت `a` فردية.
- عدد الخطوات = log₂(a) → الزمن = **O(log a)**

### 📊 مقارنة

| العدد a | Naive (O(a)) | Russian (O(log a)) |
| ------- | ------------ | ------------------ |
| 4       | 4            | 2                  |
| 8       | 8            | 3                  |
| 16      | 16           | 4                  |
| 1024    | 1024         | 10                 |

### 🧠 كيف تميز بين O(N) و O(log N)

- `O(N)`: إذا تم إنقاص العدد بمقدار 1 كل مرة.

```python
while x > 0:
    x = x - 1
```

- `O(log N)`: إذا تم تقسيم العدد إلى النصف كل مرة.

```python
while x > 0:
    x = x // 2
```

---

## 🇬🇧 English Version

### ✅ Naive Multiplication

```python
def naive(a, b):
    z = 0
    while a > 0:
        z = z + b
        a = a - 1
    return z
```

- Idea: Add `b`, `a` times.
- Time: Each iteration has 2 steps (add and subtract).
- Total steps = `a` → Time = **O(a)**

### ✅ Russian Peasant Multiplication

```python
def russian(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z = z + y
        x = x // 2
        y = y * 2
    return z
```

- Idea: Divide `a` by 2 and double `b` each iteration.
- If `a` is odd, add `b` to result.
- Total steps = log₂(a) → Time = **O(log a)**

### 📊 Comparison

| a value | Naive (O(a)) | Russian (O(log a)) |
| ------- | ------------ | ------------------ |
| 4       | 4            | 2                  |
| 8       | 8            | 3                  |
| 16      | 16           | 4                  |
| 1024    | 1024         | 10                 |

### 🧠 How to Recognize Time Complexity

- `O(N)`: When number is decreased by 1 each iteration.

```python
while x > 0:
    x = x - 1
```

- `O(log N)`: When number is divided by 2 each iteration.

```python
while x > 0:
    x = x // 2
```

# You can Test

```python
import time

def naive(a, b):
    z = 0
    while a > 0:
        z = z + b
        a = a - 1
    return z

def russian(a, b):
    z = 0
    while a > 0:
        if a % 2 == 1:
            z = z + b
        a = a // 2
        b = b * 2
    return z

# اختبار الأداء
a = 100000
b = 5

start = time.time()
naive(a, b)
end = time.time()
print("Naive Time:", end - start)

start = time.time()
russian(a, b)
end = time.time()
print("Russian Time:", end - start)
```
