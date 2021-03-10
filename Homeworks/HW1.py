"""
lines of 8-9: defined the lists
line of 11: merged the lists
line 12: sorted the elements of new "even" list
lines of 14-16: set a "for" loop on i as index, in line 15 i did the multiply work and in line 16 printed the newest elements out 
"""

even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)  # here i merge the lists
even.sort()  # here i sort the elements

for i in range(10):
    even[i] *= 2  # this line does multiply work
    print(even[i])  # and this prints the newest elements out
