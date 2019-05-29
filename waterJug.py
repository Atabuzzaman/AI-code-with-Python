def pour(jug1, jug2):
    print(jug1,'\t', jug2)
    if jug2 is 2:
        return
    elif jug2 is 4:
        pour(0, jug1)
    elif jug1 != 0 and jug2 is 0:
        pour(0, jug1)
    elif jug1 is 2:
        pour(jug1, 0)
    elif jug1 < 3:
        pour(3, jug2)
    elif jug1 < (4 - jug2):
        pour(0, (jug1 + jug2))
    else:
        pour(jug1 - (4 - jug2), (4 - jug2) + jug2)

print("JUG1\tJUG2")
pour(0, 0)