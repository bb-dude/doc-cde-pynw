

import os

hostname = "localhost" #example
#response = os.system("ping -n 1 " + hostname)
response = os.system("ping " + hostname)
#and then check the response...
if response == 0:
    print(hostname, 'is up!')
else:
    print(hostname, 'is down!')

respnzbb = os.system("ifconfig -a")
print respnzbb
