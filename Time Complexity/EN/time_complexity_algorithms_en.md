
# Time Complexity in Algorithms

In computer science, **Time Complexity** is a measure that expresses how much time a given algorithm takes to run, based on the size of its inputs. The goal of measuring time complexity is to understand the algorithm's performance in different scenarios.

### 1. **O(1)** - **Constant Time**
**O(1)** means constant complexity, which means the time taken by the code does not depend on the size of the input. No matter how large the data, the time remains constant.

#### Example Code:
```python
def get_first_element(lst):
    return lst[0]
```

In this example, accessing the first element of the list takes constant time.

#### Use Cases:

* Accessing the first element of a list.
* Retrieving a value from a dictionary using a key.

---

### 2. **O(n)** - **Linear Time**

**O(n)** means linear complexity, which means the time increases directly with the size of the input. If the input size increases, the time taken by the code will increase accordingly.

#### Example Code:
```python
def print_elements(lst):
    for item in lst:
        print(item)
```

In this example, we are iterating over each element in the list, so the time depends on the number of elements.

#### Use Cases:

* Iterating over all elements in a list or collection.
* Checking each character in a string.

---

### 3. **O(n²)** - **Quadratic Time**

**O(n²)** means quadratic complexity. The time increases at a rate proportional to the square of the input size. This usually occurs when we have nested operations for every pair of elements.

#### Example Code:
```python
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
```

In this example, we have two nested loops that compare and swap elements in the list, resulting in quadratic time complexity **O(n²)**.

#### Use Cases:

* Sorting algorithms like **Bubble Sort** and **Selection Sort**.
* Comparing all elements in an array with each other.

---

### 4. **O(n log n)** - **Linearithmic Time**

**O(n log n)** means linear logarithmic complexity. The time increases at a rate higher than **O(n)** but lower than **O(n²)**. This usually occurs in algorithms that divide the data into parts.

#### Example Code:
```python
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1
```

In this example, the algorithm splits the list into two parts and then merges them in a sorted manner. Each split takes **O(log n)** time, and with **n** splits, the total time becomes **O(n log n)**.

#### Use Cases:

* Sorting algorithms like **Merge Sort** and **Quick Sort**.
* Some operations that divide the inputs into equal parts.

---

### 5. **O(2^n)** - **Exponential Time**

**O(2^n)** means exponential complexity, where the time increases very rapidly with the size of the input. This typically occurs in algorithms that try every possible combination.

#### Example Code:
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

In this example, the algorithm computes the Fibonacci series using recursion. The large number of recursive calls leads to exponential time complexity **O(2^n)**.

#### Use Cases:

* Some **Brute Force** algorithms.
* Algorithms that explore trees or graphs using recursion.

---

### 6. **O(log n)** - **Logarithmic Time**

**O(log n)** means logarithmic complexity, where the time increases much more slowly compared to **O(n)** or **O(n²)**. This happens in algorithms that progressively divide the input into smaller parts.

#### Example Code:
```python
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

In this example, the algorithm searches for an element in a sorted list using **binary search**, where the search space is halved at each step. Hence, the time complexity is **O(log n)**.

#### Use Cases:

* Binary search in sorted lists.
* Some tree search algorithms.

---

### How to Choose n in Code?

The result **n** refers to the size of the input the algorithm deals with, such as:

* The number of elements in a list.
* The number of characters in a string.
* The number of points in a data set.

#### Example:

* If you have a list of numbers (e.g., 10 numbers), then **n** is 10.
* If you have a string of 50 characters, then **n** is 50.

---

### Conclusion:

A good understanding of **Time Complexity** helps in optimizing the performance of algorithms and code in general. When writing code, always try to consider how the input size will affect performance and choose the algorithm that best suits the use case.
