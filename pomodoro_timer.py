import time
from colorama import Fore

def work_time () :
    '''Work time calculation'''

    pomodoro_time = 25
    while pomodoro_time != 0 :
        print(Fore.GREEN+f"Remaining working time : {pomodoro_time}"+Fore.RESET)
        pomodoro_time -= 1
        time.sleep(60)
    return pomodoro_time


def free_time():
    '''Rest time calculation'''

    rest = 5
    while rest != 0 :
        print(Fore.YELLOW+f"Remaining rest time : {rest}"+Fore.RESET)
        rest -= 1
        time.sleep(60)
    return rest