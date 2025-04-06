# q: what does zip do?
# a: it combines two lists into a list of tuples
# show me code for a zip
l1 = [1, 2, 3, 4, 5]
l2 = ["a", "b", "c", "d", "e"]
for i in zip(l1, l2):
    print(i)
# show output from code above
# (1, 'a')
# (2, 'b')
# (3, 'c')
# (4, 'd')
# (5, 'e')
