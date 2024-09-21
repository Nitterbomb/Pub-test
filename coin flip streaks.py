import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    results = []
    for i in range(100):
        result = random.randint(0, 1)
        if result == 0:
            results.append("H")
        else:
            results.append("T")
    # Code that checks if there is a streak of 6 heads or tails in a row.        
    for j in range(93):
        if (results[j] == "T" and results[j+1] == "H" and results[j+2] == "H" and results[j+3] == "H" and results[j+4] == "H" and results[j+5] == "H" and results[j+6] == "H" and results[j+7] == "T") or (results[j] == "H" and results[j+1] == "T" and results[j+2] == "T" and results[j+3] == "T" and results[j+4] == "T" and results[j+5] == "T" and results[j+6] == "T" and results[j+7] == "H"):
            numberOfStreaks += 1
    
print('Chance of streak: %s%%' % (numberOfStreaks / 10000))


