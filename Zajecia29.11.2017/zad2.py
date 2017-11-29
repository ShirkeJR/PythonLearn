import subprocess

dirStr = """K1
    K2
    K3
        K4
    K5
    K6"""


outl = subprocess.call(
    ["mkdir" + x for x in dirStr.splitlines()], shell= True
)

print outl