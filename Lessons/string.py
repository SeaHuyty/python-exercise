# Strings
course = 'Python For Beginner'
         #012345 which (t) stand on the 2nd. Maybe every programming languages start from number 0. Note that space does not have the number.
print(course.upper()) # This operator upper all the letters in (course).
print(course.lower()) # This operator lower all the letters in (course).
print(course.find('t')) # This operator uses to find the place number of a letter.
# Or we can find a whole word
print(course.find('For')) # It'll show -1 if there ain't the letter or number.
print(course.replace('For', '4')) # It'll replace nothing if it ain't there.
print('Python' in course) # This (in) operator uses to find if the word or letter is there or not? it'll display True or False.
print('python' in course)