'''
Created on Dec 31, 2021

@author: justi
'''

#This is a progress bar that is based off of the number of segments and how much time is inbetween the filling of the segments. 
#I made this to have visual output to make sure my program was still running and not hanging.
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
            print('')
            break
            
        sleep(SleepTime)
        bar[count] = '▰'
        count += 1
    
