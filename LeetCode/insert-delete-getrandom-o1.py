import random


class RandomizedSet:

    def __init__(self):
        self._set = []
        self._pos = {}

    def insert(self, val: int) -> bool:
        if self._pos.get(val, None) is None:
            self._set.append(val)
            self._pos[val] = len(self._set) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if self._pos.get(val, None) is not None:
            lst = self._set.pop()
            v_idx = self._pos[val]
            del self._pos[val]
            if lst == val:
                return True
            self._set[v_idx] = lst
            self._pos[lst] = v_idx
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self._set)


def hydrate():
    res = [None]
    rs = RandomizedSet()
    for o, v in zip(ops, vals):
        if o == 'insert':
            res.append(rs.insert(*v))
        elif o == 'remove':
            res.append(rs.remove(*v))
        elif o == 'getRandom':
            res.append(rs.getRandom())
    return res


ops = ["RandomizedSet","insert","insert","insert","insert","insert","remove","insert","getRandom","insert","remove"]
vals = [[],[0],[2],[1],[1],[1],[0],[0],[],[1],[2]]

print(hydrate())
