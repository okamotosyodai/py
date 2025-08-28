scores = [80,90,75,60,95]
total = 0
avrage = 0
for s in scores:
    total += s
    avg = total / len(scores)
print('合計点:',total)
print('平均点:',avg)
