a ={'a', 'b','c','d','g','f'}
b ={'l', 'm','o','h','b','c'}
c ={'h', 'c','k','i','j','f','d'}

i=(c.difference((a.intersection(b)).union(a.intersection(c))))
ii=(a.intersection(c))
iii=(a.intersection(b).union(c.intersection(b)))
iv=(a.intersection(c)).difference(b)
v=list(ii.intersection(b))
vi=list(b.difference(a.union(c)))
print("a= ",a)
print("b= ",b)
print("c= ",c)
print("=================================================================")
#a. How many elements are there in set A and B
print("How many elements are there in set A and B")
print(len(a.union(b)), "elements are present within A and B")
print("Elements: ", a.union(b))
print("================================================================")
#b. How many elements are there in B that is not part of A and C
print("How many elements are there in B that is not part of A and C")
print(len(b.difference(c.union(a))), "are part of B but not in A and or C")
print("Elements: ", b.difference(c.union(a)))
print("===============================================================")
#show the following
#i. [h, i, j, k]
#ii. [c, d, f]
#iii. [b, c, h]
#iv. [d, f]
#v. [c]
#vi. [l, m, o]
print("i.  ", sorted(i))
print("ii. ", sorted(ii))
print("iii.", sorted(iii))
print("iv. ", sorted(iv))
print("v.  ", v)
print("vi. ", sorted(vi))
