
# 🔢 Multiplication Algorithms Comparison: Naive vs Russian Peasants

## 📌 Overview

This document explains and compares two multiplication algorithms: the **Naive method** (repeated addition) and the **Russian Peasants method** (based on halving and doubling). It also discusses the efficiency of using binary shifts vs traditional arithmetic operations.

---

## 🧠 Naive Algorithm (Repeated Addition)

### 🔍 How it works:
- This method simply **adds the number `b` repeatedly `a` times**.
- Straightforward, but can be slow for large numbers.

### 🔢 Python Code

```python
def start(a, b):
    z = 0
    while a > 0:
        z = z + b
        a = a - 1
    return z

print(start(3, 2))  # Output: 6
```

---

## ⚙️ Russian Peasants Algorithm (Bitwise Multiplication)

### 🔍 How it works:
- Repeatedly halve `x`, double `y`.
- If `x` is odd, add `y` to the result.

### 🔢 Python Code

```python
def Russian_Peasants_Algorithm(a, b):
    x = a
    y = b
    z = 0
    t = 0
    while x > 0:
        if x % 2 == 1:
            z = z + y
        y = y << 1  # Double y using bit shift
        x = x >> 1  # Halve x using bit shift
        t += 1
        print(z)
    return z, t

print(Russian_Peasants_Algorithm(5, 4))  # Output: (20, steps)
```

---

## 📊 Comparison Table

| Feature                | Naive Algorithm                  | Russian Peasants Algorithm       |
|------------------------|----------------------------------|----------------------------------|
| Core Mechanism         | Repeated addition                | Bitwise halving/doubling         |
| Performance            | Slow for large `a`               | Faster for large numbers         |
| Bitwise Optimization   | ❌ Not used                      | ✅ Yes                           |
| Number of Operations   | `a` additions                    | ≈ log₂(`a`) iterations            |
| Space Efficiency       | ✅ Simple                        | ✅ Simple                        |

---

## ⏱️ Why Russian Algorithm is Faster

- Naive method depends on how big `a` is → more repetitions.
- Russian method divides `x` by 2 each time → far fewer steps.
- Bitwise shifts (`<<`, `>>`) are faster than arithmetic operations.

---

## 💡 Shift vs Arithmetic

| Operation       | Shift Equivalent | Performance | Notes                       |
|-----------------|------------------|-------------|-----------------------------|
| Multiply by 2   | `x << 1`         | Faster      | CPU-optimized binary shift  |
| Divide by 2     | `x >> 1`         | Faster      | Ignores decimal (floor)     |
| Manual multiply | `x * 2`          | Slower      | Arithmetic operation        |
| Manual divide   | `x // 2`         | Slower      | Integer division            |

> ✅ **Conclusion**: Bitwise operations (`<<`, `>>`) are faster and preferred in optimized code.

---

# 🇸🇦 الفرق بين طريقتي الضرب: التقليدية وطريقة الفلاحين الروس

## 🧾 نظرة عامة

هذا الملف يوضح الفرق بين طريقتين للضرب:  
- الطريقة التقليدية (Naive): تعتمد على الجمع المتكرر  
- طريقة الفلاحين الروس (Russian Peasants): تعتمد على القسمة على 2 والضرب في 2 بطريقة ثنائية

---

## 🔢 الطريقة التقليدية (Naive)

### 📌 طريقة العمل:
- نقوم بجمع العدد `b` بعدد مرات يساوي `a`.
- سهلة، لكنها بطيئة للأعداد الكبيرة.

### 💻 كود بايثون

```python
def start(a, b):
    z = 0
    while a > 0:
        z = z + b
        a = a - 1
    return z

print(start(3, 2))  # الناتج: 6
```

---

## 🧮 طريقة الفلاحين الروس

### 📌 طريقة العمل:
- نقسم `x` على 2، ونضرب `y` في 2 في كل خطوة.
- إذا كان `x` عدد فردي → نضيف `y` إلى الناتج `z`.

### 💻 كود بايثون

```python
def Russian_Peasants_Algorithm(a, b):
    x = a
    y = b
    z = 0
    t = 0
    while x > 0:
        if x % 2 == 1:
            z = z + y
        y = y << 1
        x = x >> 1
        t += 1
        print(z)
    return z, t

print(Russian_Peasants_Algorithm(5, 4))  # الناتج: (20, عدد الخطوات)
```

---

## 📊 جدول المقارنة

| الخاصية                 | الطريقة التقليدية (Naive)          | طريقة الفلاحين الروس            |
|-------------------------|------------------------------------|----------------------------------|
| آلية العمل              | جمع متكرر                         | قسمة ×2 وضرب ×2 ثنائي           |
| الأداء                  | بطيئة للأرقام الكبيرة             | أسرع بكثير                      |
| استخدام التحويل الثنائي | ❌ لا يوجد                         | ✅ نعم                           |
| عدد الخطوات             | يساوي قيمة `a`                    | تقريبًا log₂(`a`) خطوات         |
| البساطة                 | ✅ بسيطة                           | ✅ بسيطة                         |

---

## ✅ لماذا طريقة الروس أسرع؟

- الطريقة التقليدية تعتمد على عدد التكرارات = `a`
- طريقة الروس تقلل `x` للنصف كل مرة، مما يقلل عدد التكرارات
- استخدام الإزاحة الثنائية أسرع من العمليات الحسابية

---

## ⚡ الإزاحة مقابل العمليات التقليدية

| العملية         | الإزاحة المكافئة | الأداء     | ملاحظات                        |
|------------------|-------------------|------------|--------------------------------|
| ضرب ×2          | `x << 1`          | أسرع       | يتم تنفيذها بسرعة على المعالج |
| قسمة ÷2         | `x >> 1`          | أسرع       | بدون كسور (تقريب لأسفل)       |
| ضرب يدوي ×2     | `x * 2`           | أبطأ       | عملية حسابية                   |
| قسمة يدوية ÷2   | `x // 2`          | أبطأ       | عملية حسابية                   |

> ✅ **الخلاصة**: الإزاحة الثنائية (`<<`, `>>`) أسرع ومناسبة للكودات الفعالة.
