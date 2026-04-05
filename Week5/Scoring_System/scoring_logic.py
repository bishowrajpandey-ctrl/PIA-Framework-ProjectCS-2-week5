
scores = {
    "Legal": 3,
    "Ethical": 2,
    "Data Protection": 3
}

total = sum(scores.values())
average = total / len(scores)

print("Scores:", scores)
print("Total Score:", total)
print("Average Score:", round(average, 2))
