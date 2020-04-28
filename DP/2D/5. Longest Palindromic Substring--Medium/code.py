#https://leetcode.com/problems/longest-palindromic-substring/
s='babad'

#brute fouce O(n^3)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ''  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j-i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m
#DP O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #memo[i][j]->s[i:j]is valid
        memo=[[False]*(n+1) for n in range(len(s)+1)]
        for i in range(len(s)+1):
            memo[i][i]=True
        for i in range(1,len(s)+1):
            memo[i][i-1]=True

        
        for j in range(2,len(s)+1):
            for i in range(j-1):
                memo[j][i]=memo[j-1][i+1]and s[j-1]==s[i]

        cur=[0,0]
        for j in range(len(s)+1):
            for i in range(j):
                if memo[j][i] and (j-i)>(cur[0]-cur[1]):
                    cur=[j,i]

        return s[cur[1]:cur[0]]

