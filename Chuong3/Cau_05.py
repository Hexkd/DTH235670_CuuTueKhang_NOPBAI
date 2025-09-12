class Method:
    def __init__(self, i, j, k):
            self.i = i
            self.j = j
            self.k = k
    def Execute(self):
        if i < j:
            if j < k:
                i = j
            else:
                j = k
        else:
            if j > k:
                j = i
            else:
                i = k

ch = "a"

i = 3
j = 5
k = 7
for index in range(6):
    print("(",chr(ord(ch) + index), ") i =", i, ", j =", j, ", k =", k, ".")
    Method(i, j ,k)
    print("\t——> i =", i, ", j =", j, ", k =", k, "\n\n")