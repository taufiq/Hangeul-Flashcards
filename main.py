from gtts import gTTS
from playsound import playsound
import os, random, codecs, tkinter
from tkinter import *

learnt = codecs.open('learn.txt', 'r','utf-8')
learntDict = dict()

for i in learnt.read().splitlines():
    j = i.split(',')
    koreanList = []
    for k in j[1:]:
        koreanList.append(k.strip())
        learntDict[j[0]] = koreanList

totalSize = len(learntDict);
currIndex = 0
currKey = ""
windowSize = 400

randomKeyList =random.sample(list(learntDict), len(learntDict))

def returnTitle(currIndex, totalSize):
    return str(currIndex + 1) + ' out of ' + str(totalSize)


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

top = Tk()

def checkAnswer(i, answer):
    if answer not in learntDict[i]:
        tts = gTTS(text=', '.join(learntDict[i]), lang='ko')
        tts.save('speech.mp3')
        os.system('speech.mp3')
        answerStatus.config(text = 'Wrong!')
        tts = gTTS(text=answer, lang='ko', slow=True)
        tts.save('wrong.mp3')
        os.system('wrong.mp3')
    else:
        learntDict[i].pop(learntDict[i].index(answer))
        answerStatus.config(text = "Correct! Other ways to say them are: {}".format(', '.join(learntDict[i])))
        tts = gTTS(text=answer + ' ' +  ', '.join(learntDict[i]), lang='ko', slow=True)
        tts.save('speech.mp3')
        os.system('speech.mp3')

def setWidgets():
    hangeulText.config(text=randomKeyList[currIndex])
    titleText.config(text=returnTitle(currIndex, totalSize))

def nextQuestion():
    global currIndex, currentKey
    currIndex += 1
    setWidgets()

#Hygiene
top.title('Hangeul Learner')
top.wm_minsize(windowSize,windowSize)

#Title to indicate current question
titleText = Label(top, text=returnTitle(currIndex, totalSize))
answerStatus = Label(top)
#Button to go to next question
nextButton = Button(top, text='Next', command=lambda: nextQuestion())
checkButton = Button(top, text='Check', command=lambda: checkAnswer(randomKeyList[currIndex], englishEntry.get()))
#Text in Hangeul
hangeulText = Label(top, text="Hello")
#Entry for English
englishEntry = Entry(top)
#Text to say if answer is right or wrong

#To draw widgets
titleText.pack(side = TOP)
nextButton.pack(side = BOTTOM)
hangeulText.pack(side = TOP)
englishEntry.pack(side = TOP)
checkButton.pack(side = BOTTOM)
answerStatus.pack(side = TOP)

setWidgets()
#End of loop
top.mainloop()


