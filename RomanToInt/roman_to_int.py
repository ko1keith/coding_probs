class RomanToInt:
    def romanToInt(self, roman):
        dict_roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        roman_arr = [char for char in roman]
        rom_rev = []
        
        for rom in roman_arr:
            rom_rev.insert(0, rom)
        
        total = 0
        skip = False
        #iterate length of roman chars
        for i in range(len(rom_rev)):
            if skip:
                skip = False
                continue
            #last element
            elif i == (len(rom_rev) - 1):
                total += dict_roman[rom_rev[i]]
            else:   
                if dict_roman[rom_rev[i]] > dict_roman[rom_rev[i + 1]]: 
                    total += dict_roman[rom_rev[i]] - dict_roman[rom_rev[i + 1]]
                    skip = True
                else:
                    total += dict_roman[rom_rev[i]]
                    skip = False

        return total
    