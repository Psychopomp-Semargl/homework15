import module1
module1.say_hi2(3)

from module1 import say_hi as sh
print(sh())

sh()