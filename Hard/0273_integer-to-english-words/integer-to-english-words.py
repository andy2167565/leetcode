class Solution:
    def numberToWords(self, num: int) -> str:
#======== <Solution 1> ========#
        if not num: return 'Zero'
        Ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        Teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        Tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        Thousands = ['', 'Thousand', 'Million', 'Billion']
        ans, count = [], 0
        while num:
            num, digit = divmod(num, 10)
            q, r = divmod(count, 3)
            if not r:
                last = next((s for s in reversed(ans) if s), None)
                if last in Thousands:
                    ans.remove(last)
                ans.extend([Thousands[q] * (q > 0), Ones[digit]])
            elif digit and r == 2:
                ans.extend(['Hundred', Ones[digit]])
            else:
                if digit == 1:
                    ans.append(Teens[Ones.index(ans.pop())])
                else:
                    ans.append(Tens[digit])
            count += 1
        return ' '.join(reversed(list(filter(None, ans))))

#======== <Solution 2> ========#
        Ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        Teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        Tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        def get_part(number):
            result = []
            if number >= 100:
                hundred, number = divmod(number, 100)
                result.extend([Ones[hundred], 'Hundred'])
            if 10 <= number < 20:
                result.append(Teens[number - 10])
            else:
                ten, number = divmod(number, 10)
                if ten: result.append(Tens[ten])
                if number: result.append(Ones[number])
            return ' '.join(result)
        ans = []
        if not num: return 'Zero'
        if num >= 10**9:
            part, num = divmod(num, 10**9)
            ans += [get_part(part), 'Billion']
        if num >= 10**6:
            part, num = divmod(num, 10**6)
            ans += [get_part(part), 'Million']
        if num >= 10**3:
            part, num = divmod(num, 10**3)
            ans += [get_part(part), 'Thousand']
        if num:
            ans += [get_part(num)]
        return ' '.join(ans)

#======== <Solution 3> ========#
        To19 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        Tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        Thousands = {
            10**9: 'Billion',
            10**6: 'Million',
            10**3: 'Thousand'
        }
        def words(n):
            if n < 20:
                return To19[n - 1: n]
            if n < 100:
                return [Tens[n // 10 - 2]] + words(n % 10)
            if n < 1000:
                return [To19[n // 100 - 1], 'Hundred'] + words(n % 100)
            else:
                for i in Thousands.keys():
                    if n // i:
                        return words(n // i) + [Thousands[i]] + words(n % i)
        return ' '.join(words(num)) or 'Zero'

#======== <Solution 4> ========#
        mapping = {
            1e9: 'Billion', 1e6: 'Million', 1e3: 'Thousand', 1e2: 'Hundred',
            90: 'Ninety', 80: 'Eighty', 70: 'Seventy', 60: 'Sixty',
            50: 'Fifty', 40: 'Forty', 30: 'Thirty', 20: 'Twenty',
            19: 'Nineteen', 18: 'Eighteen', 17: 'Seventeen', 16: 'Sixteen',
            15: 'Fifteen', 14: 'Fourteen', 13: 'Thirteen', 12: 'Twelve',
            11: 'Eleven', 10: 'Ten', 9: 'Nine', 8: 'Eight',
            7: 'Seven', 6: 'Six', 5: 'Five', 4: 'Four',
            3: 'Three', 2: 'Two', 1: 'One', 0: 'Zero'
        }
        def dp(n):
            if n <= 20: return mapping[n]
            for div in mapping.keys():
                q, r = divmod(n, div)
                if not q: continue
                s1 = dp(q) + " " if div >= 100 else ""
                s2 = " " + dp(r) if r else ""
                return s1 + mapping[div] + s2
        return dp(num)
