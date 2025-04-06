**Question**. You have three integer variables x, y and z. If you perform x + y - z, would the result be different from y - z + x?


**A**: No, the result would not be different. The associative property of addition,  states that if numbers are not grouped, then it does not change their sum. 

**Question**. Can you make a difference in the calculation sequence using parentheses with the integers? eg, 5 - (3 + 2)

**A**: Yes, using parentheses can alter the result of an expression. Parentheses in Python (and in Mathematics and many other programming languages) indicate priority and change the order of operations. In the expression 5 - (3 + 2), for example, the calculation inside the parentheses is done first (3 + 2 equals 5), then the subtraction is performed (5 - 5 equals 0).

**Question**. Would addition have higher precedence over subtraction?

**A**: No, in Python and most programming languages, addition and subtraction have the same precedence level, and they are evaluated from left to right. Therefore, an expression like 5 - 3 + 2 would first evaluate 5 - 3 to get 2, then add 2 to get 4.