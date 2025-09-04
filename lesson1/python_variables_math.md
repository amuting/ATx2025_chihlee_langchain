# Python 變數與數學運算講義

## 目錄
1. [變數的基本概念](#變數的基本概念)
2. [變數的命名規則](#變數的命名規則)
3. [基本資料型態](#基本資料型態)
4. [數學運算](#數學運算)
5. [運算優先順序](#運算優先順序)
6. [練習範例](#練習範例)

## 變數的基本概念

### 什麼是變數？
變數是程式設計中用來儲存資料的容器，可以想像成一個有名字的盒子，裡面可以放各種類型的資料。

### 變數的宣告與賦值
```python
# 基本語法
變數名稱 = 值

# 範例
name = "小明"
age = 18
height = 175.5
is_student = True
```

## 變數的命名規則

### 命名規則
1. **只能包含**：字母、數字、底線(_)
2. **不能以數字開頭**
3. **區分大小寫**：`name` 和 `Name` 是不同的變數
4. **不能使用關鍵字**：如 `if`, `for`, `while` 等

### 好的命名範例
```python
student_name = "小明"      # 使用底線分隔單字
age = 18                  # 簡潔明瞭
total_score = 95.5        # 描述性名稱
is_active = True          # 布林值使用 is_ 開頭
```

### 不好的命名範例
```python
1name = "小明"            # 不能以數字開頭
student-name = "小明"     # 不能使用連字號
if = "條件"               # 不能使用關鍵字
```

## 基本資料型態

### 1. 整數 (int)
```python
age = 18
year = 2025
temperature = -5
```

### 2. 浮點數 (float)
```python
height = 175.5
weight = 65.8
pi = 3.14159
```

### 3. 字串 (str)
```python
name = "小明"
message = '你好，世界！'
address = """台北市
信義區
101大樓"""
```

### 4. 布林值 (bool)
```python
is_student = True
is_working = False
```

### 5. 檢查資料型態
```python
age = 18
print(type(age))          # 輸出: <class 'int'>

name = "小明"
print(type(name))          # 輸出: <class 'str'>
```

## 數學運算

### 基本運算符號

| 運算符號 | 名稱 | 範例 | 結果 |
|---------|------|------|------|
| `+` | 加法 | `5 + 3` | `8` |
| `-` | 減法 | `10 - 4` | `6` |
| `*` | 乘法 | `6 * 7` | `42` |
| `/` | 除法 | `15 / 3` | `5.0` |
| `//` | 整數除法 | `17 // 3` | `5` |
| `%` | 取餘數 | `17 % 3` | `2` |
| `**` | 次方 | `2 ** 3` | `8` |

### 運算範例
```python
# 基本四則運算
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"加法: {a} + {b} = {a + b}")
print(f"減法: {a} - {b} = {a - b}")
print(f"乘法: {a} * {b} = {a * b}")
print(f"除法: {a} / {b} = {a / b}")
print(f"整數除法: {a} // {b} = {a // b}")
print(f"餘數: {a} % {b} = {a % b}")
print(f"次方: {a} ** {b} = {a ** b}")
```

### 複合運算
```python
# 複合賦值運算符
x = 10
print(f"初始值: x = {x}")

x += 5    # 等同於 x = x + 5
print(f"x += 5: {x}")

x -= 3    # 等同於 x = x - 3
print(f"x -= 3: {x}")

x *= 2    # 等同於 x = x * 2
print(f"x *= 2: {x}")

x /= 4    # 等同於 x = x / 4
print(f"x /= 4: {x}")
```

## 運算優先順序

### 優先順序（由高到低）
1. **括號** `()`
2. **次方** `**`
3. **乘法、除法、取餘數** `*`, `/`, `//`, `%`
4. **加法、減法** `+`, `-`

### 範例說明
```python
# 運算優先順序範例
result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}")        # 結果: 14 (先算 3*4=12，再加2)

result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}")      # 結果: 20 (先算括號內 2+3=5，再乘4)

result3 = 2 ** 3 + 1
print(f"2 ** 3 + 1 = {result3}")       # 結果: 9 (先算 2**3=8，再加1)

result4 = 10 / 2 + 3 * 2
print(f"10 / 2 + 3 * 2 = {result4}")   # 結果: 11 (先算 10/2=5 和 3*2=6，再加5+6)
```

## 練習範例

### 練習1：基本計算
```python
# 計算圓的面積和周長
radius = 5
pi = 3.14159

area = pi * radius ** 2
circumference = 2 * pi * radius

print(f"半徑: {radius}")
print(f"面積: {area:.2f}")
print(f"周長: {circumference:.2f}")
```

### 練習2：溫度轉換
```python
# 攝氏轉華氏
celsius = 25
fahrenheit = (celsius * 9/5) + 32

print(f"攝氏 {celsius}°C = 華氏 {fahrenheit}°F")
```

### 練習3：購物計算
```python
# 購物車計算
item1_price = 150
item2_price = 200
item3_price = 80

subtotal = item1_price + item2_price + item3_price
tax = subtotal * 0.05  # 5% 稅金
total = subtotal + tax

print(f"商品小計: ${subtotal}")
print(f"稅金 (5%): ${tax:.2f}")
print(f"總計: ${total:.2f}")
```

## 常見錯誤與注意事項

### 1. 型態錯誤
```python
# 錯誤示範
age = "18"
result = age + 5        # 錯誤！字串不能與整數相加

# 正確做法
age = int("18")         # 轉換為整數
result = age + 5        # 正確
```

### 2. 除零錯誤
```python
# 錯誤示範
result = 10 / 0         # 錯誤！除數不能為零

# 正確做法
divisor = 0
if divisor != 0:
    result = 10 / divisor
else:
    print("除數不能為零")
```

### 3. 浮點數精度問題
```python
# 注意浮點數的精度
result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")         # 可能輸出: 0.30000000000000004

# 使用 round() 函數處理
rounded_result = round(result, 2)
print(f"四捨五入後: {rounded_result}")   # 輸出: 0.3
```

## 總結

本講義涵蓋了Python變數和數學運算的基本概念：

1. **變數**是儲存資料的容器，有特定的命名規則
2. **基本資料型態**包括整數、浮點數、字串、布林值
3. **數學運算**支援四則運算、次方、取餘數等
4. **運算優先順序**決定了運算的執行順序
5. **複合運算符**可以簡化程式碼

建議多練習這些概念，並嘗試解決實際問題來加深理解。

---

*最後更新：2025年*
