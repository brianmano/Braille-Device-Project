from components.image_reading import *
from components.image_taking import *

image_taking()

results = image_reading('./images/temp.png')
print(results)