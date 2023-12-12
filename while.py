
# go variable used to keep program running
# programs stops when user inputs -1 
# "try:" to prevent strings causing errors and ending the loop 

go = True

# This empty list is for getting the values the user inputs in

average = []
while go:
    num = (input("Give me a number "))
    
    # This empty list to convert str values to int for the average calculation

    sec = []

    if num == -1 or num == "-1":
        go = False
        for i in range(0, len(average)):
            sec.append(int(average[i]))
        Sum = sum(sec)
        mean = Sum / len(sec)
        print(f"Total : {Sum}")
        print(f"Number of values : {len(sec)}")
        print(f"The average of the numbers you provided are {mean}")
            
    try:
        int(num)
        average.append(num)
    except ValueError:
        print("No")
        num

    


    