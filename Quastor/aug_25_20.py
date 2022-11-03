"""
https://quastor.substack.com/p/alexa-are-you-hiring
"""

def reverse(s, start, end):
    n = len(s)
    for i in range((end-start+1)//2):
        s[start+i], s[-1-(n-end-1)-i] = s[-1-(n-end-1)-i], s[start+i]
    return s

def reverseWords(s: str) -> str:
    st, ed = -1, -1
    for i in range(len(s)):
        if st == -1 and s[i] != ' ':
            st = i
        if ed == -1 and s[-1-i] != ' ':
            ed = len(s)-1-i
        if i > 0:
            if s[i] == ' ' and s[i-1] == ' ':
                s[i-1] = None
    s = s[st:ed+1]
    s = [c for c in s if c is not None]
    n = len(s)
    if n < 3:
        return s
    s = reverse(s, 0, n-1)
    start = 0
    for end in range(n):
        if s[end] == ' ':
            s = reverse(s, start, end-1)
            start = end + 1
    if start < n-1:
        s = reverse(s, start, n-1)
    return s

tc1 = list("Alice likes Bob")
ans1 = list("Bob likes Alice")
tc2 = list("This is a test!")
ans2 = list("test! a is This")
tc3 = list("This Is")
ans3 = list("Is This")
tc4 = []
ans4 = []
tc5 = ['Yo']
ans5 = ['Yo']

print(reverseWords(tc1) == ans1)
print(reverseWords(tc2) == ans2)
print(reverseWords(tc3) == ans3)
print(reverseWords(tc4) == ans4)
print(reverseWords(tc5) == ans5)