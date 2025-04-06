# what can you tell me about loops in Python?
# 1. for loop
# show me code for a for loop
for i in range(10):
    print(i)

# show me code for a for loop with a list
l = [1, 2, 3, 4, 5]
for i in l:
    print(i)
# 2. while loop
# show me code for a while loop
i = 0
while i < 10:
    print(i)
    i += 1
# 3. break
# show me code for a break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1
# 4. continue
# show me code for a continue
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
# 5. pass
# q: what does "pass" keyword do?
# a: it does nothing

# show me code for a pass
i = 0
while i < 10:
    i += 1
    if i == 5:
        pass
    print(i)
# 6. range
# show me code for a range
for i in range(10):
    print(i)

# 7. enumerate
# show me code for a enumerate
l = [1, 2, 3, 4, 5]
for i, v in enumerate(l):
    print(f"index: {i}, value: {v}")
# q: what is the difference between range and enumerate?
# a: enumerate returns the index and the value

# 8. zip
# q: what does zip do?
# a: it combines two lists into a list of tuples
# show me code for a zip
l1 = [1, 2, 3, 4, 5]
l2 = ["a", "b", "c", "d", "e"]
for i, v in zip(l1, l2):
    print(f"index: {i}, value: {v}") # index: 1, value: a
# 9. list comprehension
# q: what is list comprehension?
# a: it is a way to create a list from another list
# show me code for a list comprehension
l = [i for i in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l)
# 10. nested loops
# show me code for a nested loop
for i in range(10):
    for j in range(10):
        print(f"i: {i}, j: {j}")
# 11. nested loops with list comprehension
# 12. nested loops with enumerate
# 13. nested loops with zip
# 14. nested loops with enumerate and list comprehension
# 15. nested loops with zip and list comprehension
# 16. nested loops with enumerate and zip
# 17. nested loops with enumerate, zip and list comprehension
# 18. nested loops with enumerate, zip and list comprehension

# what does range() do?
# it creates a range of numbers




# for leep with index and increment
# show me code for a for loop with index, increment with 2 for each iteration
for i in range(0, 10, 2):
    print(i)



