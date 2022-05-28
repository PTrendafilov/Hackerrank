n = int(input())
scores = list(map(int, input().rstrip().split()))
max_score = scores[0]
min_score = scores[0]
breaking_max = 0
breaking_min = 0
for score in scores:
    if max_score < score:
        max_score = score
        breaking_max += 1
    if min_score > score:
        min_score = score
        breaking_min += 1
print([breaking_max, breaking_min])
