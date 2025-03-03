from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
                error = error + 1
    return error
   
def speed_time(time_s,time_e,userinput):
    time_t = time_e - time_s
    time_R = round(time_t,2)
    speed = len(userinput) / time_R
    return round(speed)
     

test =["A quick brown fox jumps over the lazy dog",
"My name is Parth","Welcome to the world of Python"]
test1 = r.choice(test)
print("***** typing Speed *****")
print(test1)
print()
print()
time_1 = time()
testinput=input("Type the above sentence: ")
time_2 = time()

print('Speed:',speed_time(time_1,time_2,testinput), "w/s")
print('Error:',mistake(test1,testinput))
