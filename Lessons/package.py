# Package: Is basically another way to organize our code. A package is a container for multiple modules.
#          A package is a directory or folder. Packages are extremely important, especially when you work with a framework like django.
#          We use Django to build web applications with Python.
# Create a new folder in a folder named ".venv" and name it (__init__.py), when Python see the file's name, it treats the file as package.
# This is the code in package name "ecommerce">file name "shipping.py":
def calc_shipping():
    print("calc_shipping")
# After create the folder and modules in files:
import ecommerce.shipping # Here you have to call the package's name and then the module's name.
                          # This is how to import a function in a module in a package.
ecommerce.shipping.calc_shipping()
# Or We can write like this: (Shorter code)
from ecommerce.shipping import calc_shipping
calc_shipping()

from ecommerce import shipping # This is how to import an entire module in a package.
shipping.calc_shipping() # And call a function in the module.