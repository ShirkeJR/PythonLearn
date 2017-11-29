import subprocess

try:
    compOut = subprocess.call(
        ["g++ -o file.o file.cpp"]
    )
except subprocess.CalledProcessError as ex:
    print "Kompilacja się nie powiodła: ", ex
    exit(1)

try:
    runOut = subprocess.check_call(
        ["./file.o"], shell=True
    )
    print runOut
except subprocess.CalledProcessError as ex:
    print "Uruchomienie się nie powiodło: ", ex