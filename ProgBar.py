'''
Created on Dec 31, 2021

@author: justi
'''

#You can either leave the arguments blank and it will prompt you for the number of segments/SleepTime, or you can directly input them to bypass the prompt.

from time import sleep

def ProgressBar(Segments = None, SleepTime = None, ArgumentsCanBeLeftBlankForPrompts = None):
    
    if Segments == None:
        Segments = int(input('Enter How long you want your progress bar: '))
    if SleepTime == None:
        SleepTime = float(input('How long in seconds between each bar progress: '))
    
    
    x = 0
    
    bar = []
    
    while x != Segments:
        bar.append('▱')
        x += 1
    
    count = 0
    while count != Segments + 1:
        for i in bar:
            print(i, end = '')
        
        if count == Segments:
            break
            print('')
        print('')
        sleep(SleepTime)
        bar[count] = '▰'
        count += 1
    
