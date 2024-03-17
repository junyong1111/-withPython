
for i in range(0, len(plma)):
    if plma[i] == "-":
        answer -= numbers[i+1]
    else:
        answer += numbers[i+1]
print(answer)