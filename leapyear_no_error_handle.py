#Peter J. Bloch
#1/15/2021
#Software Engineering 2 (CS 362) Winter 2020
#To run the code, please type “python3 leapyear.py” into your unix terminal and for inputs, 
# please use only numbers or blank “” or “\n” characters.

#Flowchart is on written portion of the assignment
def main():
    game = True

    while game == True:
        year = input("Please give me a year\t")
        leap_year = False

        #please note, it is written in flowchart as an if/else loop here, but I chose to simply implement exit(0) for simplicity sake
        if year == "" or year == "\n":
            print("Thank you for playing!\n")
            exit(0)
        else:
            year = int(year)

        if year%4 != 0: #This checks if the remainder after division by 4 is zero (i.e. cleanly divisible)
            leap_year = False
        else:
            if year%100 !=0:
                leap_year = True
            else:
                if year%400 ==0:
                    leap_year=True

        if leap_year == True:
            print("You have found a Leap Year!\n")
        else:
            print("You have not found a Leap Year :/\n")
    return 0

if __name__ == "__main__":
    main()