# import pyautogui
# file_1 = open("Question.txt", "r") 
# pyautogui.sleep(5)
# for lines in file_1:
#     print(lines)
#     pyautogui.write(lines)
import pyautogui
import time
time.sleep(3)
with open('Question.txt','r')as f:
    lines=f.readlines()
    for line in lines:
        print(line.lstrip())

        pyautogui.write(line.lstrip())

