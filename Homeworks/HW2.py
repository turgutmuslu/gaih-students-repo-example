# i created cv dictionary, and then created 5 empty keys which symbolizes people. I filled them with unvalued attributes by a "for" loop. Then set another "for" loop to get inputs from user. And set the last "for" loop to print CV's.

cv = {"hasan":"", "nurbanu":"", "pembe":"", "kemal":"", "reyhan":""}

for i in cv:
    cv[i] = {"name-surname":"", "age":"", "job title":"", "foreign languages":""}

for i in cv:
    for j in cv[i]:
        print(f"Please enter {j} of {i}")
        cv[i][j] = str(input())

for i in cv:
    print(f"\n{i}'s CV:")
    for j in cv[i]:
        print(f" {j}: {cv[i][j]}")
