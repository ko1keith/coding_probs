class LongestCommonPrefix(object):
  '''
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
  '''
  def longest_common_prefix(self, array):

    print(array)
    min_length = len(min(array, key=len))
    return_string = ""
    for i in range(min_length):
      # get char array of letter of each element index
      char_array = list(map(lambda x: x[i],array))
      check_if_equal = all(char == char_array[0] for char in char_array)

      if(check_if_equal):
        return_string += char_array[0]
      else:
        break
      
    return return_string

obj = LongestCommonPrefix()

output = obj.longest_common_prefix(["taesti", "testing", "testies"])
print(output)