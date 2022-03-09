# O(Nlog(N))

def is_unique(string: str):
    if len(string) <= 1:
        return True
    string = sorted(string)
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return False
    return True
