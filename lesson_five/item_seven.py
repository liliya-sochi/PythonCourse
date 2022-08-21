import json

profit = {}
firms_profit = {}
data = [firms_profit, profit]
sum_margin = 0
count_firm_avg = 0

with open("seven.txt", encoding='cp1251') as f:
    for line in f:
        name, form, salary, cost = line.split()
        margin = float(salary) - float(cost)
        if margin > 0:
            count_firm_avg = count_firm_avg + 1
            sum_margin = sum_margin + margin
            firms_profit[name] = margin
if count_firm_avg > 0:
    profit["average_profit"] = sum_margin / count_firm_avg

with open("seven.json", "w", encoding='cp1251') as write_f:
    json.dump(data, write_f)
print(f"{firms_profit} {profit}")
