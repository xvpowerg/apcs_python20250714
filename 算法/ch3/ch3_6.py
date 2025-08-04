for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for m in range(1,5):
                if j!= i and k != i and k!= j and m != k and m != j and m != i:
                    print(f"{i}{j}{k}{m}")                    
