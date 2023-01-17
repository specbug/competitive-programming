class Solution:
	def isValid(self, s: str) -> bool:
		if len(s) & 1:
			return False
		brackets = {'}': '{', ']': '[', ')': '('}
		stack = []
		for c in s:
			if c in brackets.values():
				stack.append(c)
			else:
				if not stack or stack[-1] != brackets[c]:
					return False
				stack.pop()
		return len(stack) == 0