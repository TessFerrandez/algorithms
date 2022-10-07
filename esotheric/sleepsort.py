from threading import Thread
import time


def print_number(number):
    time.sleep(number)
    print(number, end='')


def sleep_sort(nums):
    for number in nums:
        Thread(target=print_number, args=(number,)).start()


sleep_sort([3, 1, 2, 1, 2, 2, 1])
