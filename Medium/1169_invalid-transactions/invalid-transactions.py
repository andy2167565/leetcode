class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions:
            return []
        names, times, amounts, cities = [], [], [], []
        for trans in transactions:
            name, time, amount, city = trans.split(',')
            names.append(name)
            times.append(int(time))
            amounts.append(int(amount))
            cities.append(city)
        invalid = [False] * len(transactions)
        for i in range(len(transactions)):
            if amounts[i] > 1000:
                invalid[i] = True
            for j in range(i + 1, len(transactions)):
                if names[i] == names[j] and cities[i] != cities[j] and abs(times[i] - times[j]) <= 60:
                    invalid[i] = invalid[j] = True
        return [transactions[i] for i, v in enumerate(invalid) if v]
