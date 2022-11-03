class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            ab = 'abcdefghijklmnopqrstuvwxyz'
            ab_map = {k: i for i, k in enumerate(ab)}
            ans_map = dict()
            for i in strs:  # O(n)
                enc = [0] * 26
                for c in i:  # O(s)
                    enc[ab_map[c]] += 1
                enc_str = '-'.join(str(e) for e in enc)
                ans_map[enc_str] = ans_map.get(enc_str, []) + [i]
            return [v for v in ans_map.values()]