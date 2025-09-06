# Python 條件判斷和迴圈講義

## 目錄
1. [條件判斷 (if-elif-else)](#條件判斷-if-elif-else)
2. [比較運算符](#比較運算符)
3. [邏輯運算符](#邏輯運算符)
4. [for 迴圈](#for-迴圈)
5. [while 迴圈](#while-迴圈)
6. [迴圈控制語句](#迴圈控制語句)
7. [巢狀結構](#巢狀結構)
8. [練習範例](#練習範例)

---

## 條件判斷 (if-elif-else)

### 基本語法

```python
if 條件1:
    # 如果條件1為真，執行這裡的程式碼
    程式碼區塊1
elif 條件2:
    # 如果條件1為假但條件2為真，執行這裡的程式碼
    程式碼區塊2
else:
    # 如果所有條件都為假，執行這裡的程式碼
    程式碼區塊3
```

### 簡單範例

```python
# 基本 if 語句
age = 18
if age >= 18:
    print("您已成年")

# if-else 語句
score = 85
if score >= 60:
    print("及格")
else:
    print("不及格")

# if-elif-else 語句
temperature = 25
if temperature > 30:
    print("天氣很熱")
elif temperature > 20:
    print("天氣溫暖")
elif temperature > 10:
    print("天氣涼爽")
else:
    print("天氣寒冷")
```

### 縮排的重要性

```python
# 正確的縮排
if True:
    print("這行會被執行")
    print("這行也會被執行")

# 錯誤的縮排（會產生 IndentationError）
if True:
print("這行會產生錯誤")  # 縮排錯誤
```

---

## 比較運算符

### 基本比較運算符

| 運算符 | 名稱 | 範例 | 結果 |
|--------|------|------|------|
| `==` | 等於 | `5 == 5` | `True` |
| `!=` | 不等於 | `5 != 3` | `True` |
| `>` | 大於 | `5 > 3` | `True` |
| `<` | 小於 | `3 < 5` | `True` |
| `>=` | 大於等於 | `5 >= 5` | `True` |
| `<=` | 小於等於 | `3 <= 5` | `True` |

### 比較運算範例

```python
# 數值比較
a = 10
b = 20

print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")    # False
print(f"a != b: {a != b}")    # True
print(f"a > b: {a > b}")      # False
print(f"a < b: {a < b}")      # True
print(f"a >= b: {a >= b}")    # False
print(f"a <= b: {a <= b}")    # True

# 字串比較
name1 = "Alice"
name2 = "Bob"
print(f"name1 == name2: {name1 == name2}")  # False
print(f"name1 < name2: {name1 < name2}")    # True (字典序比較)
```

---

## 邏輯運算符

### 基本邏輯運算符

| 運算符 | 名稱 | 說明 | 範例 |
|--------|------|------|------|
| `and` | 且 | 兩個條件都為真 | `True and True` |
| `or` | 或 | 至少一個條件為真 | `True or False` |
| `not` | 非 | 條件取反 | `not True` |

### 邏輯運算範例

```python
# and 運算符
age = 25
has_license = True

if age >= 18 and has_license:
    print("可以開車")

# or 運算符
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("今天不用上班")

# not 運算符
is_raining = False

if not is_raining:
    print("天氣很好，可以出門")

# 複雜邏輯運算
score = 85
is_student = True
has_attendance = True

if (score >= 80 and is_student) or (score >= 90 and not is_student):
    print("成績優秀")
```

### 運算優先順序

```python
# 邏輯運算符優先順序：not > and > or
result1 = True and False or True
print(f"True and False or True = {result1}")  # True

result2 = True and (False or True)
print(f"True and (False or True) = {result2}")  # True

result3 = not True and False
print(f"not True and False = {result3}")  # False
```

---

## for 迴圈

### 基本語法

```python
for 變數 in 可迭代物件:
    # 迴圈主體
    程式碼區塊
```

### 基本範例

```python
# 遍歷字串
word = "Python"
for char in word:
    print(char)

# 遍歷列表
fruits = ["蘋果", "香蕉", "橘子"]
for fruit in fruits:
    print(f"我喜歡{fruit}")

# 遍歷範圍
for i in range(5):
    print(f"數字: {i}")

# 遍歷範圍（指定起始和結束）
for i in range(1, 6):
    print(f"數字: {i}")

# 遍歷範圍（指定步長）
for i in range(0, 10, 2):
    print(f"偶數: {i}")
```

### range() 函數詳解

```python
# range(stop) - 從0到stop-1
for i in range(5):
    print(i)  # 輸出: 0, 1, 2, 3, 4

# range(start, stop) - 從start到stop-1
for i in range(2, 7):
    print(i)  # 輸出: 2, 3, 4, 5, 6

# range(start, stop, step) - 從start到stop-1，步長為step
for i in range(0, 10, 3):
    print(i)  # 輸出: 0, 3, 6, 9

# 反向遍歷
for i in range(5, 0, -1):
    print(i)  # 輸出: 5, 4, 3, 2, 1
```

---

## while 迴圈

### 基本語法

```python
while 條件:
    # 迴圈主體
    程式碼區塊
```

### 基本範例

```python
# 基本 while 迴圈
count = 0
while count < 5:
    print(f"計數: {count}")
    count += 1

# 使用者輸入驗證
password = ""
while password != "123456":
    password = input("請輸入密碼: ")
    if password != "123456":
        print("密碼錯誤，請重試")
print("密碼正確！")

# 計算階乘
n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"{n}! = {factorial}")
```

### 避免無限迴圈

```python
# 錯誤示範 - 無限迴圈
# count = 0
# while count < 5:
#     print(f"計數: {count}")
#     # 忘記增加 count，會造成無限迴圈

# 正確做法
count = 0
while count < 5:
    print(f"計數: {count}")
    count += 1  # 記得要改變條件變數
```

---

## 迴圈控制語句

### break 語句

```python
# break - 跳出迴圈
for i in range(10):
    if i == 5:
        break  # 當 i 等於 5 時跳出迴圈
    print(i)  # 輸出: 0, 1, 2, 3, 4

# 在 while 迴圈中使用 break
count = 0
while True:  # 無限迴圈
    if count >= 5:
        break  # 跳出迴圈
    print(f"計數: {count}")
    count += 1
```

### continue 語句

```python
# continue - 跳過本次迭代，繼續下一次迭代
for i in range(5):
    if i == 2:
        continue  # 跳過 i=2 的迭代
    print(i)  # 輸出: 0, 1, 3, 4

# 只印出奇數
for i in range(10):
    if i % 2 == 0:
        continue  # 跳過偶數
    print(f"奇數: {i}")  # 輸出: 1, 3, 5, 7, 9
```

### else 子句

```python
# for-else 結構
for i in range(3):
    print(f"迴圈: {i}")
else:
    print("迴圈正常結束")  # 只有在迴圈正常結束時才會執行

# 如果使用 break，else 不會執行
for i in range(5):
    if i == 3:
        break
    print(f"迴圈: {i}")
else:
    print("這行不會被執行")

# while-else 結構
count = 0
while count < 3:
    print(f"計數: {count}")
    count += 1
else:
    print("while 迴圈正常結束")
```

---

## 巢狀結構

### 巢狀 if 語句

```python
# 巢狀 if 語句
age = 20
has_license = True
has_insurance = True

if age >= 18:
    if has_license:
        if has_insurance:
            print("可以開車")
        else:
            print("需要保險才能開車")
    else:
        print("需要駕照才能開車")
else:
    print("年齡不足，不能開車")
```

### 巢狀迴圈

```python
# 巢狀 for 迴圈 - 九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} × {j} = {i * j}", end="\t")
    print()  # 換行

# 巢狀迴圈 - 繪製圖形
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print("*", end="")
    print()

# 輸出:
# *
# **
# ***
# ****
# *****
```

### 巢狀迴圈中的 break 和 continue

```python
# 巢狀迴圈中的 break
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            break  # 只跳出內層迴圈
        print(f"i={i}, j={j}")

# 使用標籤跳出外層迴圈
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            break  # 跳出內層迴圈
        print(f"i={i}, j={j}")
    else:
        continue  # 只有內層迴圈正常結束時才執行
    break  # 跳出外層迴圈
```

---

## 練習範例

### 練習1：成績等級判斷

```python
# 根據分數判斷等級
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# 測試
scores = [95, 85, 75, 65, 55]
for score in scores:
    grade = get_grade(score)
    print(f"分數: {score}, 等級: {grade}")
```

### 練習2：質數判斷

```python
# 判斷一個數是否為質數
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 找出 1 到 20 的所有質數
print("1 到 20 的質數:")
for num in range(1, 21):
    if is_prime(num):
        print(f"{num} 是質數")
```

### 練習3：猜數字遊戲

```python
import random

# 猜數字遊戲
def guess_number():
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("我想到一個 1 到 100 之間的數字，請猜猜看！")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"第 {attempts + 1} 次猜測 (還有 {max_attempts - attempts} 次機會): "))
            attempts += 1
            
            if guess == target:
                print(f"恭喜！你猜對了！答案是 {target}")
                print(f"你總共用了 {attempts} 次猜中")
                return
            elif guess < target:
                print("太小了！")
            else:
                print("太大了！")
                
        except ValueError:
            print("請輸入有效的數字！")
            attempts -= 1
    
    print(f"遊戲結束！答案是 {target}")

# 執行遊戲
guess_number()
```

### 練習4：計算平均分數

```python
# 計算多個學生的平均分數
def calculate_average():
    students = []
    
    # 輸入學生資料
    while True:
        name = input("請輸入學生姓名 (輸入 'done' 結束): ")
        if name.lower() == 'done':
            break
        
        try:
            score = float(input(f"請輸入 {name} 的分數: "))
            students.append({"name": name, "score": score})
        except ValueError:
            print("請輸入有效的分數！")
    
    if not students:
        print("沒有輸入任何學生資料")
        return
    
    # 計算平均分數
    total_score = sum(student["score"] for student in students)
    average = total_score / len(students)
    
    # 顯示結果
    print("\n=== 成績報告 ===")
    for student in students:
        status = "及格" if student["score"] >= 60 else "不及格"
        print(f"{student['name']}: {student['score']} ({status})")
    
    print(f"\n平均分數: {average:.2f}")
    print(f"總學生數: {len(students)}")

# 執行計算
calculate_average()
```

### 練習5：費波那契數列

```python
# 產生費波那契數列
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

# 產生前 10 個費波那契數
fib_sequence = fibonacci(10)
print("前 10 個費波那契數:")
for i, num in enumerate(fib_sequence):
    print(f"F({i}) = {num}")
```

---

## 常見錯誤與注意事項

### 1. 縮排錯誤

```python
# 錯誤示範
if True:
print("這行會產生 IndentationError")

# 正確做法
if True:
    print("這行是正確的")
```

### 2. 比較運算符錯誤

```python
# 錯誤示範
if x = 5:  # 錯誤！使用了賦值運算符
    print("錯誤")

# 正確做法
if x == 5:  # 正確！使用了比較運算符
    print("正確")
```

### 3. 無限迴圈

```python
# 錯誤示範 - 無限迴圈
# count = 0
# while count < 5:
#     print(count)
#     # 忘記增加 count

# 正確做法
count = 0
while count < 5:
    print(count)
    count += 1  # 記得要改變條件變數
```

### 4. 邏輯運算符錯誤

```python
# 錯誤示範
if age >= 18 && has_license:  # 錯誤！Python 使用 and 不是 &&
    print("可以開車")

# 正確做法
if age >= 18 and has_license:  # 正確！
    print("可以開車")
```

---

## 總結

本講義涵蓋了Python條件判斷和迴圈的重要概念：

1. **條件判斷**：使用 `if-elif-else` 結構進行條件分支
2. **比較運算符**：用於比較兩個值的大小關係
3. **邏輯運算符**：用於組合多個條件
4. **for 迴圈**：用於遍歷可迭代物件
5. **while 迴圈**：用於重複執行直到條件不滿足
6. **迴圈控制**：使用 `break` 和 `continue` 控制迴圈流程
7. **巢狀結構**：在條件判斷和迴圈中嵌套其他結構

這些概念是程式設計的基礎，建議多練習實際問題來加深理解。記住要正確使用縮排，避免常見的語法錯誤！

---

*最後更新：2025年*
