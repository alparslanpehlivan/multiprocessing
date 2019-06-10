
import os
from multiprocessing import Process, current_process


def square(number):
    result = number * number

    #process_id = os.getpid()
    #print(f"Process ID: {process_id}")

    process_name= current_process().name
    print(f"Process Name: {process_name}")

    #print("The number "+str(number) + " squares to "+ str(result))

    print(f"The number {number} squares to {result}.")

if __name__ == "__main__":

    processes = []
    numbers =[1,2,3,4]

    for number in numbers:
        process = Process(target=square, args=(number,))
        processes.append(process)

        # Processes are spawned by creating a Process object and
        # then calling its start() method
        process.start()