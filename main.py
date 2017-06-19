from gtts import gTTS
from playsound import playsound
import os, random, codecs, tkinter
from tkinter import *

learnt = codecs.open('learn.txt', 'r','utf-8')
learntDict = dict()
top = Tk()
top.title('Hangeul Learner')
englishText = Label(top, text="Hello")
englishText.pack(side = TOP)
top.mainloop()

for i in learnt.read().splitlines():
    j = i.split(',')
    koreanList = []
    for k in j[1:]:
        koreanList.append(k.strip())
    learntDict[j[0]] = koreanList

def chooseFlashCard(inputList):
    if len(inputList) == 0:
        print("That is all for today!")
        return

    randomSample = random.sample(list(inputList), len(inputList))
    i = randomSample[0]
    inputAnswer = input('What is {}?'.format(i))
    inputAnswer = inputAnswer.strip()
    if inputAnswer not in learntDict[i]:
        print("Wrong! How {} is said: {}".format(i, ', '.join(learntDict[i])))
        tts = gTTS(text=', '.join(learntDict[i]), lang='ko')
        tts.save('speech.mp3')
        os.system('speech.mp3')
        print('What you said was: {}'.format(inputAnswer))
        tts = gTTS(text=inputAnswer, lang='ko', slow=True)
        tts.save('wrong.mp3')
        os.system('wrong.mp3')
    else:
        learntDict[i].pop(learntDict[i].index(inputAnswer))
        print("Correct! Other ways to say them are: {}".format(', '.join(learntDict[i])))
        tts = gTTS(text=inputAnswer + ' ' +  ', '.join(learntDict[i]), lang='ko', slow=True)
        tts.save('speech.mp3')
        os.system('speech.mp3')
    inputList.pop(i, None)
    chooseFlashCard(inputList)

chooseFlashCard(learntDict)


