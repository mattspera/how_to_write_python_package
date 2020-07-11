# Import your Python package here
from example_project.caps import Capitals

# Within import statement above:
# 'example_project' == Package
# 'caps' == Module
# 'Capitals' == Class

def main():

    # Instantiate an object from the 'Capitals' class found within the 'caps.py' module contained within your package
    # This gives you access to the 'Captials' class methods
    capitals_obj = Capitals()

    # Convert string to uppercase with method residing within class object
    string_caps = capitals_obj.convert_to_captitals('hello, world!')
    print(string_caps)
    # HELLO, WORLD!

if __name__ == "__main__":
    main()