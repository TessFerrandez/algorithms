'''
This is an interactive problem.

You are given an array of unique strings wordlist where wordlist[i] is 6 letters long, and one word in this list is chosen as secret.

You may call Master.guess(word) to guess a word. The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word. Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have exactly 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or fewer calls to Master.guess and at least one of these guesses was secret, then you pass the test case.

ALGO:
-------------------
Guess a word - find the number of matches
Reduce the word list to only the words that have that many matches
Eventually you will only have the 6 match word left
'''
from typing import List
import random

def num_matches(word1, word2):
    return sum(1 for i in range(len(word1)) if word1[i] == word2[i])


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        while wordlist:
            index = random.randint(0, len(wordlist) - 1)
            word_to_guess = wordlist[index]
            num_right = master.guess(word_to_guess)
            if num_right == 6:
                return
            wordlist = [word for word in wordlist if num_matches(word, word_to_guess) == num_right and word != word_to_guess]


class Master():
    def __init__(self, wordlist, secret) -> None:
        self.wordlist = wordlist
        self.secret = secret
        self.num_guesses = 0

    def guess(self, word: str):
        self.num_guesses += 1
        if word not in self.wordlist:
            return -1
        return num_matches(word, self.secret)


solution = Solution()

wordlist = ["ccbazz", "eiowzz", "abcczz", "acckzz"]
master = Master(wordlist, 'acckzz')
solution.findSecretWord(wordlist, master)
print(master.num_guesses)

wordlist = ["hamada","khaled"]
master = Master(wordlist, 'hamada')
solution.findSecretWord(wordlist, master)
print(master.num_guesses)

wordlist = ["wichbx","oahwep","tpulot","eqznzs","vvmplb","eywinm","dqefpt","kmjmxr","ihkovg","trbzyb","xqulhc","bcsbfw","rwzslk","abpjhw","mpubps","viyzbc","kodlta","ckfzjh","phuepp","rokoro","nxcwmo","awvqlr","uooeon","hhfuzz","sajxgr","oxgaix","fnugyu","lkxwru","mhtrvb","xxonmg","tqxlbr","euxtzg","tjwvad","uslult","rtjosi","hsygda","vyuica","mbnagm","uinqur","pikenp","szgupv","qpxmsw","vunxdn","jahhfn","kmbeok","biywow","yvgwho","hwzodo","loffxk","xavzqd","vwzpfe","uairjw","itufkt","kaklud","jjinfa","kqbttl","zocgux","ucwjig","meesxb","uysfyc","kdfvtw","vizxrv","rpbdjh","wynohw","lhqxvx","kaadty","dxxwut","vjtskm","yrdswc","byzjxm","jeomdc","saevda","himevi","ydltnu","wrrpoc","khuopg","ooxarg","vcvfry","thaawc","bssybb","ccoyyo","ajcwbj","arwfnl","nafmtm","xoaumd","vbejda","kaefne","swcrkh","reeyhj","vmcwaf","chxitv","qkwjna","vklpkp","xfnayl","ktgmfn","xrmzzm","fgtuki","zcffuv","srxuus","pydgmq"]
master = Master(wordlist, "ccoyyo")
solution.findSecretWord(wordlist, master)
print(master.num_guesses)
