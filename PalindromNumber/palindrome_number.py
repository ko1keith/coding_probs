class PalindromeNumber:
    def isPalindrome(self, x):
        if x >= 0 and x < 10 or x < 0:
            return True
        elif x < 0:
            return False
        
        x_arr = [char for char in str(x)]
        x_arr_reverse = []
        for char in x_arr:
            x_arr_reverse.insert(0, char)
            if x_arr == x_arr_reverse:
                return True
        
        return False