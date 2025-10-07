def isPalindrome(self, s: str) -> bool:
    s=s.lower()
    s2 = ''.join([char for char in s if char.isalnum()])
    if s2==s2[::-1]:
        return True
    else:
        return False
