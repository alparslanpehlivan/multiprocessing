
import os
import time

from multiprocessing import Process, current_process


def square(numbers):
    for number in numbers:
        time.sleep(10)
        result = number * number
        print(f"The number {number} squares to {result}.")

    #process_id = os.getpid()
    #print(f"Process ID: {process_id}")

    #process_name= current_process().name
    #print(f"Process Name: {process_name}")

    #print("The number "+str(number) + " squares to "+ str(result))

if __name__ == "__main__":

    #processes = []
    processes = []
    
    number = range(100)

    for i in range(50):
        process = Process(target=square, args=(number,))
        processes.append(process)

        # Processes are spawned by creating a Process object and
        # then calling its start() method
        process.start()

    for process in processes:
        process.join()

    print("Multiprocessing complete")
