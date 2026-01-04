a=[]
for i in range(1,11):
    a.append(i)
print(f"original list:{a}")
print(f"Extracted first five elements:{a[:5:]}")
b=a[:5:]
b.reverse()
print(f"Reversed extracted elements:{b}")