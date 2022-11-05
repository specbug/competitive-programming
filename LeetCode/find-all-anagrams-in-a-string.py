class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_map = dict()
        for c in p:
            p_map[c] = p_map.get(c, 0) + 1
        s_map = dict()
        ctr = 0
        l = len(p)
        n = len(s)
        if n < l:
            return []
        ans = []
        for i in range(l):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            if s[i] in p_map and p_map[s[i]] >= s_map[s[i]]:
                ctr += 1
            if ctr == l:
                ans.append(0)
        for i in range(l, n):
            we = s[i]
            ws = s[i-l]
            if ws in p_map and p_map[ws] >= s_map.get(ws, -1):
                ctr -= 1
            if ws in s_map:
                s_map[ws] -= 1
            s_map[we] = s_map.get(we, 0) + 1
            if we in p_map and p_map[we] >= s_map[we]:
                ctr += 1
            if ctr == l:
                ans.append(i-l+1)
        return ans
