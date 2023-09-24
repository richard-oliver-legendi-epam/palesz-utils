class MyContextManager:
    def __init__(self, msg):
        self.msg = msg
        print("init", msg)

    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")


with MyContextManager("mcm") as cm:
    print(">> actual work")

""" Actual output is:
init mcm
enter
>> actual work
exit
"""
