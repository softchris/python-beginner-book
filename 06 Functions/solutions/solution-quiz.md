**Question**. How do you define a function in Python?

1. Using the `function` keyword. 

2. Using the `def` keyword. 

3. Using the `func` keyword. 

4. Using the `method` keyword

**A**: 2, Using the `def` keyword.

**Question**. What will be the output of the following code?

    ```python
    def add_numbers(x, y):
        return x + y

    result = add_numbers("3", "5")
    print(result)
    ```

1. 8

2. 15

3. "35"

4. Error

**A**: 3, 35. Closely observe the `"3"` and `"5"`, they are string, and you cannot perform addition operation on strings. But if you try to add two strings, the operation that is performed is called concatenation. Hence string `"3"` and string `"5"` are being concatenated resulting in `"35"`

**Question**. Can you write a function without the `return` keyword?

1. Yes 

2. No

**A**: 1, Yes. The function will automatically return a `none` which is nothing or no value and the function simply finishes.
