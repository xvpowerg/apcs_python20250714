c = 65
count = 0
for i in range(0,5):
    for j in range(0,5):
        if j == i:
            continue
        for k in range(0,5):
            if k == i or k == j:
                continue
            for l in range(0,5):
                if l == i or l == j or l == k:
                    continue
                for m in range(0,5):
                    if m == i or m == j or m == k or m == l:
                        continue
                    count += 1
                    print(f"count:{count}:{chr(c+i)},{chr(c+j)},{chr(c+k)},{chr(c+l)},{chr(c+m)}")

