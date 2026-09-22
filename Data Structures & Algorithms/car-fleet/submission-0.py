class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = sorted([x for x in zip(position, speed)])
        for pos, s in pos_speed:
            t = (target - pos) / s
            while stack and t >= stack[-1]:
                stack.pop()
            stack.append(t)
        return len(stack)