import time
import surmath
from imp import reload

print("the prog entering into sleeping state")
time.sleep(1)
reload(surmath)
print("this is the last line")
surmath.f1()

