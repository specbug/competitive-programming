class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        set_map = dict()
        char_group = dict()
        n = len(s1)
        ans = ''
        l = 0

        for i in range(n):
            if not all(c in char_group for c in [s1[i], s2[i]]):
                if not any(c in char_group for c in [s1[i], s2[i]]):
                    group = {s1[i], s2[i]}
                    h = l
                    l += 1
                    set_map[h] = group
                    char_group[s1[i]] = h
                    char_group[s2[i]] = h
                else:
                    if s1[i] not in char_group:
                        h = char_group[s2[i]]
                        set_map[h].add(s1[i])
                        char_group[s1[i]] = h
                    else:
                        h = char_group[s1[i]]
                        set_map[h].add(s2[i])
                        char_group[s2[i]] = h
            else:
                if char_group[s1[i]] != char_group[s2[i]]:
                    set_map[char_group[s1[i]]].update(set_map[char_group[s2[i]]])
                    g2 = set_map[char_group[s2[i]]]
                    del set_map[char_group[s2[i]]]
                    for e in g2:
                        char_group[e] = char_group[s1[i]]

        for k, g in set_map.items():
            set_map[k] = sorted(g)[0]

        for i in baseStr:
            e = set_map.get(char_group.get(i, -1), i)
            if ord(i) < ord(e):
                ans += i
            else:
                ans += e

        return ans