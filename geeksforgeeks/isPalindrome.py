def isPalindrome(s):
    #code here
    print(s[::-1])
    if s == s[::-1]:
        
        return True
    else:
        return False
    
print(isPalindrome("Hello"))
print(isPalindrome("TenEt"))