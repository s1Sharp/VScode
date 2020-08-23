def odometer(mylist):
    distance = 0
    speed=0
    previoustime = 0
    time = mylist[1]
    for i in range(len(mylist)):
        if i % 2 == 0:
            speed = mylist[i]
        else:
            time = mylist [i]
            distance += (time - previoustime) * speed 
            previoustime = time 
    return distance 

mylist = [10,1,20,2,100,4]
print(odometer(mylist))