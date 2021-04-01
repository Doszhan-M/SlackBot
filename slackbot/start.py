# import subprocess

#     # отрыть скрипт bash как файл и выполнить ее из python среды
#     with open('./scripts/parse.sh', 'rb') as file:
#         script = file.read()
#     rc = subprocess.call(script, shell=True)
#     return redirect('botconfig')
a = 5
import time
def onceEveryXSeconds(seconds):                         # this creates the decorator
    def wrapper(f):                                       # decorator for given 'seconds'
        f.last_execution = 0                                                        # memorize last execution time
        def decorated(*args, **kwargs):                     # the 'decorated' function
            if f.last_execution < time.time() - seconds:
                f.last_execution = time.time()
                return f(*args, **kwargs)
        return decorated
    return wrapper


@onceEveryXSeconds(a)
def function(foo):
    print(foo)
while True:
    function("Hello again")
