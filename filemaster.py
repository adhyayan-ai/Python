import os
import time
time.sleep(3)
os.mkdir("1")
time.sleep(1)
os.mkdir("2")
time.sleep(1)
os.rmdir("2")
fi = open("Hhha.txt", "w+")
for i in range(10):
    fi.write("Hi!\n")

fi.close()

print("All done for now! ")