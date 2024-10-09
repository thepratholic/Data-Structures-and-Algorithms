'''problem statement : Given an array of n names arr of candidates in an election,where each name is a string of lowercase 
characters. A candidate name in the array represents a vote casted to the candidate. 
Print the name of the candidate that received the maximum count of votes. If there is a draw between two candidates, 
then print lexicographically smaller name.'''

class Solution:
    def winner(self,arr,n):

        d = {}
        
        for i in arr:
            if i not in d: d[i] = 1
            else: d[i] += 1
            
        
        max_votes = 0
        winner = ""
        
        for candidate, votes in d.items():
            if votes > max_votes or (votes == max_votes and candidate < winner):
                max_votes = votes
                winner = candidate
                
        return winner, max_votes
            