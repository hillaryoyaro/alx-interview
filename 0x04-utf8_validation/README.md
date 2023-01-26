## 0x04-utf8_validation

### Problem
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.


### Prototype
```python
def validUTF8(data):

```


### Example
```python
data = [197, 130, 1]
validUTF8(data) -> True

data = [235, 140, 4]
validUTF8(data) -> False

```

### Constraints
-   The input is an array of integers
-  Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
- You don’t need to handle the case where a byte is split between two integers

### Resources
-   [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
-  [Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)
