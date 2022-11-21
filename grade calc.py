score = input ('Enter your score : ')
try:
    sre = float (score)
except :
    print ('Error, please enter numeric value')
    quit()

try:
    float(score) <= 1.0
    float(score) >= 0.0
except:
    print ('Enter value between the range')
    quit()

if sre < 0.6 :
    print ('F')
elif sre >= 0.9 :
    print ('A')
elif sre >= 0.8 :
    print ('B')
elif sre >= 0.7 :
    print ('C')
elif sre >= 0.6 :
    print ('D')
