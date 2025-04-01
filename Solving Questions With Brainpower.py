from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N=len(questions)
        score= [0]*N
        for i in reversed(range(N)):
            points, brain = questions[i]
            next_i = i+1+brain
            choose = points + (score[next_i] if next_i < N else 0)
            skip = score[i+1] if i+1 < N else 0
            score[i] = max(choose, skip)
        print(score)

        return score[0]