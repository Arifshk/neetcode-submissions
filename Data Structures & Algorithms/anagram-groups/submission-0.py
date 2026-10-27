class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_letters = {}
        for word in strs:
            sorted_key = "".join(sorted(word))
            if sorted_key in sorted_letters:
                sorted_letters[sorted_key].append(word)
            if sorted_key not in sorted_letters:
                    sorted_letters[sorted_key] = [word]

        return list(sorted_letters.values())
           
           


        