scores =  list(map(int,input().split(" ")) )
print(scores)
score_sum = 0
counts = len(scores)
score_max = 0
score_min = 100

for i in range(counts):
    score_sum += scores[i]
    if scores[i] > score_max  :
        score_max = scores[i]
    if scores[i] < score_min:
        score_min = scores[i]
print(f"總分:{score_sum}")        
print(f"Max:{score_max}")    
print(f"Min:{score_min}")    
