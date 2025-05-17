class Solution:
    def findMaximumCookieStudents(self, Student, Cookie):
        #your code goes here
        n = len(Student)
        m = len(Cookie)

        Student.sort()
        Cookie.sort()

        l,r = 0,0

        while l < n and r < m:
            if Cookie[r] >= Student[l]:
                l += 1

            r += 1

        return l 