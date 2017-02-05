"""
a = ["Hello","World","!"]
for i, x in enumerate(a):     # Iterating over list index and value pairs (enumerate)  
    print(i, ":", x)


b = {"a":1, "b":2, "c":3, "d":4}
for c, d in b.items():      #  Iterating over dictionary key and value pairs (dict.items)
    print(c,":",d)
"""

f = ["India", "China", "USA", "UK", "Australia"]
gold = [2, 100, 99, 50, 20]
silver = [10, 50, 100, 40, 80]
for m, n, o in zip(f, gold, silver):
    print(m, "Gold:- ", n,"Silver:- ", o)


h = zip(f, gold)
print(list(h))

ans = []
ans.append("Hello")
print(ans)

