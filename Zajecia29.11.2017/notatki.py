import subprocess
import os

#Uwaga, na windowsie nie ryzykuj.

with open(os.devnull, "w") as devnull:
    outll = subprocess.call(
        ["dir"], shell= True)


outl = subprocess.call(
    ["dir"], shell = True)

print outll