
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = [1 if len(s) >= 1 else 0] 
        starting_position = 0
        while starting_position < len(s):
            letters_sean = []
            for length_of_sequence, letter in enumerate(s[starting_position:],1):
                if letter not in letters_sean:
                    max_length.append(length_of_sequence)
                    letters_sean.append(letter)
                else:
                    break
            starting_position += 1
        return max(max_length)

sol = Solution()
print(sol.lengthOfLongestSubstring("au"))