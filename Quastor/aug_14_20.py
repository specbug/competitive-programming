"""
You’re given an array of strings as input. The strings will only contain lowercase letters from `a-z`. Group all the anagrams in the array together and return the resulting array. An anagram is a word that can be formed by rearranging the letters of another word.

`Input: [“yx“, “abe”, “act”, “eab”, “x“, “eba“, “tca“, “xy“]`
`Output: [`
`[“abe”, “eab”, “eba”],`
`[“act”, “tca”],`
`[“xy”, “yx”],`
`[“x”]`
`]`
"""


def group_anagrams(a):
    """Group anagrams"""
    ab = 'abcdefghijklmnopqrstuvwxyz'
    ab_map = {k: i for i, k in enumerate(ab)}
    ans_map = dict()
    for i in a:  # O(n)
        enc = [0] * 26
        for c in i:  # O(s)
            enc[ab_map[c]] += 1
        enc_str = ''.join(str(i) for i in enc)
        ans_map[enc_str] = ans_map.get(enc_str, []) + [i]
    return [v for v in ans_map.values()]
