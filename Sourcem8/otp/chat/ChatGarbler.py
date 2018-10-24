import string
import random
from otp.otpbase import OTPLocalizer

class ChatGarbler:

    def garble(self, avatar, message):
        newMessage = ''
        numWords = random.randint(1, 7)
        wordlist = OTPLocalizer.ChatGarblerDefault
        for i in xrange(1, numWords + 1):
            wordIndex = random.randint(0, len(wordlist) - 1)
            newMessage = newMessage + wordlist[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '

        return newMessage

    def garbleSingle(self, avatar, message, wordlist):
        newMessage = ''
        numWords = 1
        for i in xrange(1, numWords + 1):
            wordIndex = random.randint(0, len(wordlist) - 1)
            newMessage = newMessage + wordlist[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '

        return newMessage
