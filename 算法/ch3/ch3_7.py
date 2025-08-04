for i in range(1,5):
    for j in range(1,5):
        if i == j:
            continue
        for k in range(1,5):
            if i == k or j == k:
                continue
            for m in range(1,5):
                if i == m or j == m or k ==m:
                    continue
                print(f"{i}{j}{k}{m}")
