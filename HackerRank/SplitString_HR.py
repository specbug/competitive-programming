def splitString(s):
    evenStr = ""
    oddStr = ""
    for i in range(len(s)):
        if i%2==0:
            evenStr += s[i]
        elif i%2!=0:
            oddStr += s[i]
    print(evenStr+" "+oddStr)


t = int(input())
for i in range(t):
    string = str(input())
    splitString(string)