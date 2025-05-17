class Solution:
    def maxMeetings(self, start, end):
        #your code goes here
        meetings = []

        n = len(start)
        for i in range(n):
            meetings.append([start[i], end[i]])

        meetings.sort(key=lambda x : x[1])

        count = 1
        last_meeting_end = meetings[0][1]

        for i in range(1, n):
            if meetings[i][0] > last_meeting_end:
                count += 1
                last_meeting_end = meetings[i][1]

        return count