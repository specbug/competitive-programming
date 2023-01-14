class FreqStack:
    def __init__(self):
        self._freq_map = dict()
        self._stack_map = dict()
        self.maxf = 0

    def push(self, val: int) -> None:
        self._freq_map[val] = self._freq_map.get(val, 0) + 1
        self.maxf = max(self.maxf, self._freq_map[val])
        if self._freq_map[val] not in self._stack_map:
            self._stack_map[self._freq_map[val]] = []
        self._stack_map[self._freq_map[val]].append(val)

    def pop(self) -> int:
        val = self._stack_map[self.maxf].pop()
        if len(self._stack_map[self.maxf]) == 0:
            del self._stack_map[self.maxf]
            self.maxf -= 1
        self._freq_map[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()