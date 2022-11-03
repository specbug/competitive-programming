class Solution:
    def is_substring(self, main, sub):
        return main.find(sub) != -1
    
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return self.is_substring(goal+goal, s)