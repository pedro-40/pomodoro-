try:
    from colorama import Fore
except: 
    print ("Please install colorama library")

def banner() :
    '''For start'''

    print(Fore.CYAN+"Pomodoro begins .(Good luck :)"+Fore.RESET)