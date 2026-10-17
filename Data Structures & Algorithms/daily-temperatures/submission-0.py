class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = []
        for i in temperatures:
            answer.append(0)
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                gap = i-stack[-1]
                answer[stack[-1]] = gap
                stack.pop()
            stack.append(i)
        return answer