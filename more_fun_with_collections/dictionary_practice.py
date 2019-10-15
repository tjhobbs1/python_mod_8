d = {'A':90,'B':80,'C':70,'D':60,'F':0}
print(d)
if "A" in d:
    del d["A"]
print(d)
d.update({'A':93})
print(d)
print(d['A'])
# print(d['Z'])
print(list(d))
print(sorted(d))
print('A' in d)
