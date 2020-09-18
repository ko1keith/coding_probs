class Palindrome(object):

    def isPalindrome(self, x):
        if(x < 0):
            # if x is negative, automatically return false
            return False

        # convert x to an array of individual chars so they can be compared
        x = list(str(x))

        loopLength = len(x) // 2
        #print("Loop Length: " + str(loopLength))
        for i in range(loopLength):
            # run loop for half the length of the array

            # -1 in an array index returns the last element, so compare first element to last,
            # then second to second last, etc
            if(x[i] == x[-1 - i]):
                #print(x[i] + " is equal to " + x[-1 - i])
                pass
            else:
                #print(x[i] + " is not  " + x[-1 - i])
                return False
        return True
