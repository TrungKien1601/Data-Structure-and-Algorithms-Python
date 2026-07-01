def is_palindrome(s : str) -> bool:
    l,r = 0, len(s) - 1
    while l<r:
        while l<r and not s[l].isalnum():
            l += 1
        while l<r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        
if __name__ == "__main__":
    s = input("race a car")
    res = is_palindrome(s)
    print("true" if res else "false ")  # Kết quả mong đợi: True