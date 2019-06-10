def square(number):
    result = number * number
    #print("The number "+str(number) + " squares to "+ str(result))
    print(f"The number {number} squares to {result}.")

if __name__ == "__main__":

    numbers =[1,2,3,4]

    for number in numbers:
        square(number)