light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):               # code doesnot check this condition because the statement is true in the previous statement itself. so it stops checking the furthur lines
    print("look")
print("End od code")

#...............................................................................................................................

num = 6

if(num > 2):
    print("yes")                      # yes
if(num > 3):
    print("yes")                      # yes

#Because here there are two if conditions are present 

num = 6

if(num > 2):
    print("yes")                     # yes
elif(num > 3):
    print("yes")

# here the output is only one yes because when the if condition is true it doesnot check the next condition 

#...............................................................................................................................

**Nesting

age = 30

if(age >= 18):
    if(age >= 20):
        print("cannot drive")
    else:
        print("Can drive")
else:
    print("ok")

# output is Cannot Drive 


