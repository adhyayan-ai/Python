ls = ["bob", "no", "bobby", "yes", "bob", "not really", "not really", "bobby", "no", "bob", "bob"]

d = {}
s = 0
index = -1
for i in ls:
    d[i] = ls.count(i)
print(d)

ls2 = d.values()

for i in ls2:
    s += i

divisions = []

for j in ls2:
    divisions.append(j/s)


keys = list((d.keys()))

new_d = {}

for k in keys:
    index += 1
    new_d[k] = divisions[index]



print(new_d)