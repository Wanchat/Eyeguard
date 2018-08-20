import os
import time
second = 0
minute = 0
hours = 0
start = time.time()
while(True):
    print("Simple Stopwatch(in Python) Created By Sourabh Somani...")
    print('\n\n\n\n\n\n\n')
    print('\t\t\t\t-------------')
    print('\t\t\t\t  %d : %d : %d '%(hours,minute,second))
    print('\t\t\t\t-------------')
    # time.sleep(1)
    second = time.time() - start
    second+=1
    if second > 5:
        second = 0
        minute+=1
        print('hellllo')
        start = time.time()
    # if minute == 60:
    #     minute = 0
    #     hours+=1
    # start = time.time()
    os.system('cls')