# Modules: A module contains all functions and classes. We use it to organize our code.
#          Instead of putting all the code in one file. Module helps us break it up.
def lbs_to_kg(weight):
    return weight * 0.45
def kg_to_lbs(weight):
    return weight / 0.45
import converters # We have to create a new file and name it whatever but here I name it "converters.py", then import it here.
                  # converters.py code above. You can copy it and paste it in a new file.
print(converters.kg_to_lbs(70))
# We can directly call a function in the code.
import converters
from converters import kg_to_lbs
kg_to_lbs(100) # Here we can easily call the function.