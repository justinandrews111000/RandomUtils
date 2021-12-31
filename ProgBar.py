'''
Created on Dec 31, 2021

@author: justi
'''
from time import sleep

def ProgressBar(increment = None, SleepTime = None, ArgumentsCanBeLeftBlankForPrompts = None):
    
    if increment == None:
        increment = int(input('Enter How long you want your progress bar: '))
    if SleepTime == None:
        SleepTime = float(input('How long in seconds between each bar progress: '))
    
    
    x = 0
    
    bar = []
    
    while x != increment:
        bar.append('▱')
        x += 1
    
    count = 0
    while count != increment + 1:
        for i in bar:
            print(i, end = '')
        
        if count == increment:
            break
            print('')
        print('')
        sleep(SleepTime)
        bar[count] = '▰'
        count += 1
    
