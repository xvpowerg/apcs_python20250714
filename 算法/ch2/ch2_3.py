scores =  list(map(int,input().split(" ")) )
scores.sort()
print(scores)
score_sum = sum(scores)
score_max = scores[-1]
score_min = scores[0]

print(f"總分:{score_sum}")        
print(f"Max:{score_max}")    
print(f"Min:{score_min}")    
