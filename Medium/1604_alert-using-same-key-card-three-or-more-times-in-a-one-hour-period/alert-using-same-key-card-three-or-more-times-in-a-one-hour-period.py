class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        import collections
        name_time = collections.defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hh, mm = map(int, time.split(':'))
            name_time[name].append(hh * 60 + mm)

        alert_names = set()
        for name, times in name_time.items():
            times.sort()
            for i in range(2, len(times)):
                if times[i] - times[i - 2] <= 60:
                    alert_names.add(name)
                    break

        return sorted(alert_names)
