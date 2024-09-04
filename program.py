import os

def check():
    # Check environment variable
    if not 'COMP290' in os.environ:
        print("No COMP290 environment variable set. Make sure it's capitalized!")
        return
    if not os.environ['COMP290'] == "SUPER_COOL_VALUE":
        print(f"COMP290 environment variable should be set to SUPER_COOL_VALUE, but is instead: {os.environ['COMP290']}")

    # Check file structure
    if not os.getcwd() == "/project":
        print(f"This program should have an active directory of /project, but instead is {os.getcwd()}")

check()