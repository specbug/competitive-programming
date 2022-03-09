# O(N)

def is_unique(string: str):
    if len(string) <= 1:
        return True
    freq_map = dict()
    for c in string:
        if freq_map.get(c, None):
            return False
        freq_map[c] = 1
    return True
