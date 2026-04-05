def risk_level(score):
    if score >= 4:
        return "Low"
    elif score >= 2.5:
        return "Medium"
    else:
        return "High"

scores = [3, 2, 3]

for s in scores:
    print("Score:", s, "Risk:", risk_level(s))
