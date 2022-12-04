class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
#======== <Solution 1> ========#
        for i in range(len(sentence)):
            if sentence[i] == ' ' and sentence[i - 1] != sentence[i + 1]:
                return False
        return sentence[0] == sentence[-1]

#======== <Solution 2> ========#
        words = sentence.split()
        for i in range(len(words)):
            if words[i - 1][-1] != words[i][0]:
                return False
        return True

#======== <Solution 3> ========#
        words = sentence.split()
        return all(w[-1] == words[(i + 1) % len(words)][0] for i, w in enumerate(words))
