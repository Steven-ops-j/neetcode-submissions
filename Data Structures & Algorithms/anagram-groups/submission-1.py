import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = string.ascii_lowercase
        output = [strs]
        for letter in alphabet:
            new_output = []
            for group in output:
                count_to_ind = {}
                for word in group:
                    count = word.count(letter)
                    if count_to_ind.get(count) == None:
                        new_output.append([word])
                        count_to_ind[count] = len(new_output) - 1
                    else:
                        new_output[count_to_ind[count]].append(word)
            output = new_output 
        return output