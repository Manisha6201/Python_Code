# -*- coding: utf-8 -*-
"""Tuple Questions Python Assignment-1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UMqnv_2QKMYD-uCk3UI3ivzODdQRsMeR
"""

#Q1. Python program to Find the size of a Tuple

import sys

Mak2001 = ("A", 1, "B", 2, "C", 3)
Mak2002 = ("Delhi", "AAFT", "Noida", "Data", "Manisha")
Mak2003 = ((1, "Creat"), ( 2, "A"), (3, "New"), (4, "Page"))

print(str(sys.getsizeof(Mak2001)) + "bytes")
print(str(sys.getsizeof(Mak2002)) + "bytes")
print(str(sys.getsizeof(Mak2003)) + "bytes")

#Q2. Maximum and Minimum K elements in Tuple

Mak2001 = (1, 2, 3, 4, 5, 6)

K = 2

my_result = []
Mak2001 = list(Mak2001)
temp = sorted(Mak2001)

for idx, val in enumerate(temp):
   if idx < K or idx >= len(temp) - K:
      my_result.append(val)
my_result = tuple(my_result)

print(my_result)

#Q3. Create a list of tuples from given list having number and its cube in each tuple

Mak2001 = [1, 2, 3, 4, 5, 6]
my_result = [(val, pow(val, 3)) for val in Mak2001]
print(my_result)

#Q4. Adding Tuple to List and vice – versa

Mak2001 = [1, 2, 3, 4, 5, 6]

Mak2002 = (7, 8)

Mak2001 += Mak2002

print(str(Mak2001))

#Q5. Sum of tuple elements

Mak2001 = (7, 8)
print(sum(Mak2001))

#Q6. Modulo of tuple elements

Mak2001 = (1, 2, 3, 4)
Mak2002 = (5, 6, 7, 8)

res = tuple(map(mod, Mak2001, Mak2002))

print(str(res))

#Q7. Row-wise element Addition in Tuple Matrix

Mak2001 = [[("Nothing", 3), ("but", 3)], [("Creativity", 1)], [("Creat", 5), ("thing", 1)]]

Mak2002 = [6, 7, 8]

res = [[sub + (Mak2002[idx], ) for sub in val] for idx, val in enumerate(Mak2001)]

print(str(res))

#Q8. Update each element in tuple list

Mak2001 = (10, 20, 30, 40)

Mak2002 = list(Mak2001)

updated_Mak2002 = [item + 100 for item in Mak2002]

updated_tuple = tuple(updated_Mak2002)

print(updated_tuple)

#Q9. Multiply Adjacent elements

Mak2001 = (7, 8, 0 ,3, 45, 3, 2, 22)

my_result = tuple(i * j for i, j in zip(Mak2001, Mak2001[1:]))

print(my_result)

#Q10. Join Tuples if similar initial element

Mak2001 = [(43, 15), (66, 98), (64, 80), (14, 9), (47, 17)]

my_result = []
for sub in Mak2001:
   if my_result and my_result[-1][0] == sub[0]:
      my_result[-1].extend(sub[1:])
   else:
      my_result.append([ele for ele in sub])
my_result = list(map(tuple, my_result))

print(my_result)

#Q11. All pair combinations of 2 tuples

from itertools import product
N = 2

my_result = [ele for ele in product(range(1, N + 1), repeat = N)]

print(my_result)

#Q12. Remove Tuples of Length K

Mak2001 = [(32, 51), (22,13 ), (94, 65, 77), (70, ), (80, 61, 13, 17)]

K = 2

my_result = [ele for ele in Mak2001 if len(ele) != K]

print(my_result)

#Q13. Remove Tuples from the List having every element as None

Mak2001 = [(2, None, 12), (None, None, None), (23, 64), (121, 13), (None, ), (None, 45, 6)]

my_result = [sub for sub in Mak2001 if not all(elem == None for elem in sub)]

print(my_result)

#Q14. Sort a list of tuples by second Item

def tuple_sort(Mak2001):
   return(sorted(Mak2001, key = lambda x: x[1]))
Mak2001 = [('bill', 11), ('rick', 45), ('john', 89), ('liv', 25)]

print(tuple_sort(Mak2001))

#Q15. Sort Tuples by Total digits

def count_tuple_digits(row):
   return sum([len(str(element)) for element in row])

Mak2001 = [(32, 14, 65, 723), (13, 26), (12345,), (137, 234, 314)]

Mak2001.sort(key = count_tuple_digits)

print(Mak2001)

#Q16. Elements frequency in Tuple

from collections import defaultdict

Mak2001 = (4, 5, 4, 5, 6, 6, 5, 5, 4)

res = defaultdict(int)
for ele in Mak2001:

	res[ele] += 1

print(str(dict(res)))

#Q17. Filter Range Length Tuples

Mak2001 = [(4, ), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]

i, j = 2, 3

res = [sub for sub in Mak2001 if len(sub) >= i and len(sub) <= j]

print(str(res))

#Q18. Assign Frequency to Tuples

Mak2001 = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]

res = [(*key, val) for key, val in Counter(Mak2001).items()]

print(str(res))

#Q19. Records with Value at K index

Mak2001 = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]

ele = 3

K = 1

res = []
for x, y, z in Mak2001:
	if y == ele:
		res.append((x, y, z))

print(str(res))

#Q20. Test if tuple is distinct

Mak2001 = (11, 14, 54, 0, 58, 41)

my_result = len(set(Mak2001)) == len(Mak2001)

print(my_result)

#Q21. Python program to find tuples which have all elements divisible by K from a list of tuples

Mak2001 = [(45, 90, 135), (71, 92, 26), (2, 67, 98)]

K = 5

my_result = [sub for sub in Mak2001 if all(ele % K == 0 for ele in sub)]

print(str(my_result))

#Q22. Python program to find Tuples with positive elements in List of tuples

Mak2001 = [(56, 43), (-31, 21, 23), (51, -65, 26), (24, 56)]

my_result = [sub for sub in Mak2001 if all(elem >= 0 for elem in sub)]

print(my_result)

#Q23.  Count tuples occurrence in list of tuples

Alist = [[('Mon', 'Wed')], [('Mon')], [('Tue')],[('Mon', 'Wed')] ]

res = collections.defaultdict(int)
for elem in Alist:
   res[elem[0]] += 1
print(res)

#Q24. Removing duplicates from tuple

Mak2001 = [(11, 14), (0, 78), (33, 11), (0, 78)]

my_unique_list = list(set([i for i in Mak2001]))

print(my_unique_list)

#Q25. Remove duplicate lists in tuples (Preserving Order)

Mak2001 = ([1, 21, 34] , [11, 0, 98], [45, 67, 56], [11, 0, 98])

temp_val = set()

my_result = [elem for elem in Mak2001 if not(tuple(elem) in temp_val or temp_val.add(tuple(elem)))]

print(my_result)

#Q26. Extract digits from Tuple list

Mak2001 = [(67, 2), (34, 65), (212, 23), (17, 67), (18, )]

N = 2

my_result = [sub for sub in Mak2001 if all(len(str(ele)) == N for ele in sub)]

print(my_result)

#Q27. Cross Pairing in Tuple List

Mak2001 = [('My', 'Name'), ('Is', 'Data'), ('Hello', 'Come'), ('goodwill', 'Jill')]
Mak2002 = [('My', 'AAFT'), ('Is', 'Science'), ('Hello', 'Here'), ('a', 'b')]

Mak2001.sort()
Mak2002.sort()

my_result = [(a[1], b[1]) for a, b in zip(Mak2001, Mak2002) if a[0] == b[0]]

print(my_result)

#Q28. Consecutive Kth column Difference in Tuple List

Mak2001 = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]

K = 1

res = []
for idx in range(0, len(Mak2001) - 1):

	res.append(abs(Mak2001[idx][K] - Mak2001[idx + 1][K]))

print(str(res))

#Q29. Kth Column Product in Tuple List

def prod_compute(my_val) :
   my_result = 1
   for elem in my_val:
      my_result *= elem
   return my_result

Mak2001 = [(51, 62, 75), (18,39, 25), (81, 19, 99)]

K = 2

my_result = prod_compute([sub[K] for sub in Mak2001])

print(my_result)

#Q30. Flatten tuple of List to tuple

Mak2001 = ([5, 6], [6, 7, 8, 9], [3])

res = tuple(sum(Mak2001, []))

print(str(res))

#Q31. Flatten Tuples List to String

Mak2001 = [(11, 14), (54, 56), (98, 0), (13, 76)]

my_result = str(Mak2001).strip('[]')

print(my_result)

#Q32. Python program to sort a list of tuples alphabetically

def sort_tuple_vals(Mak2001):
   Mak2001.sort(key = lambda x: x[0])
   return Mak2001
Mak2001 = [("Hey", 18), ("Jane", 33), ("Will", 56),("Nysa", 35), ("May", "Pink")]

print(sort_tuple_vals(Mak2001))

#Q33. Combinations of sum with tuples in tuple list

Mak2001 = [( 67, 45), (34, 56), (99, 123), (10, 56)]

res = [(b1 + a1, b2 + a2) for (a1, a2), (b1, b2) in combinations(Mak2001, 2)]

print(str(res))

#Q34. Custom sorting in list of tuples

def tuple_sort(Mak2001):
   Mak2001.sort(key = lambda x: x[1])
   return Mak2001

Mak2001 = [('Will', 100), ('John', 67), ('Harold', 86), ('Jane', 35)]

print(tuple_sort(Mak2001))