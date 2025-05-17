class Solution:
    def lemonadeChange(self, bills):
        #your code goes here
        n = len(bills)
        hasFive, hasTen = 0, 0
        for i in range(n):
            if bills[i] == 5:
                hasFive += 1

            elif bills[i] == 10:
                if hasFive >= 1:
                    hasFive -= 1
                    hasTen += 1
                else:
                    return False

            else:
                if hasFive >= 1 and hasTen >= 1:
                    hasFive -= 1
                    hasTen -= 1
                elif hasFive >= 3:
                    hasFive -= 3
                else:
                    return False

        return True