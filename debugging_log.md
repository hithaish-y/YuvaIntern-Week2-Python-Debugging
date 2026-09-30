# Debugging Log - Expense Tracker CLI

## 1. Initial Review
The original program adds, displays, deletes and saves expenses. I reviewed file I/O, loops, conditions, input conversion, list indexing and exception handling.

## 2. Bugs Found and Fixes

### Bug 1: Wrong empty data type
Before:
```python
except FileNotFoundError:
    return {}
```
The program expects a list because it calls append(). The fix returns [].

### Bug 2: Invalid amount crashes the program
Before:
```python
amount = float(input("Amount: "))
```
Text input raises ValueError. The fix uses try/except and checks that the amount is greater than zero.

### Bug 3: Empty expense names
An empty name was accepted. The fix checks `if not title` and returns with a validation message.

### Bug 4: Delete uses the wrong index
Before:
```python
number = int(input("Enter expense number to delete: "))
del expenses[number]
```
The UI numbers start at 1 but Python indexes start at 0. The fix validates the range and uses `expenses.pop(number - 1)`.

### Bug 5: Invalid delete input
Non-numeric input raised ValueError. The fix catches ValueError.

### Bug 6: Out-of-range delete
A number such as 99 could raise IndexError. The fix checks `1 <= number <= len(expenses)`.

### Bug 7: Invalid JSON
Malformed JSON could raise JSONDecodeError. The fix catches it and starts with an empty list.

### Bug 8: File encoding
The corrected version explicitly uses UTF-8 for file operations.

## 3. Debugging Process
1. Reviewed the original source.
2. Identified risky file, input and indexing sections.
3. Reproduced each issue with controlled inputs.
4. Recorded the observed behavior and root cause.
5. Applied one fix at a time.
6. Re-ran the relevant scenario after each fix.
7. Refactored repeated validation into clear function-level responsibilities.
8. Performed final functional checks.

## 4. Test Cases
- Add valid expense: works.
- Empty name: rejected.
- Amount `abc`: rejected without crashing.
- Amount `0`: rejected.
- View empty list: displays no-expenses message.
- Delete item `1`: deletes the first displayed item.
- Delete `99`: rejected.
- Delete `abc`: rejected without crashing.
- Missing JSON file: starts with empty list.
- Invalid JSON: warning is shown and program continues.
- Exit: saves data and exits.

## 5. Final Result
The corrected application keeps the original intended functionality while improving error handling, input validation, data consistency, indexing correctness, readability and file handling. It uses only the Python standard library.
