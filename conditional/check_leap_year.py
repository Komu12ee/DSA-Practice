num=int(input("Enter the year "))
if num%100==0:
    if num%400==0:
        print("Leap year")
    else:
        print("Not Leap year")
elif num%4==0:
    print("Leap year")
else:
    print("Not Leap year")