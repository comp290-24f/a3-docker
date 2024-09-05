import importlib.util
import os

def check():
    # Check if bs4 is installed
    package_name = 'bs4'

    spec = importlib.util.find_spec(package_name)
    if spec is None:
        print(f"{package_name} is not installed")
    else:
        print("beautifulsoup4 successfully installed!")

    # Check environment variable
    if 'COMP290' in os.environ:
        env_var_value = os.environ['COMP290']
        if env_var_value == 'fb009':
            print(f"COMP290 environment variable set correctly!")
        else:
            print(
                f"COMP290 environment variable set to '{os.environ['COMP290']}' but should be 'fb009'"
            )
    else:
        print("COMP290 environment variable not set.")

    # Check file structure
    if not os.getcwd() == "/a03":
        print(f"This program should have a working directory of /a03, but instead is {os.getcwd()}")

check()
