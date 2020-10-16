class Solution:
    def find_rec(self, n1, n2, s, found):
        if s == '' and found:
            return True
        n3 = str(n1 + n2)
        idx = min(len(s), len(n3))
        if s[0:idx] == n3:
            return self.find_rec(n2, int(n3), s[idx:], True)
        return False
    
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n-1):
            n1 = int(num[0:i])
            if str(n1) !=  num[0:i]:
                break
            for j in range(i+1, n):
                n2 = int(num[i:j])
                if str(n2) != num[i:j]:
                    break
                found = self.find_rec(n1, n2, num[j:], False)
                if found: return True
        return False
