from sys import argv
from os.path import exists 

script, from_file, to_file = argv 

print(f"This script \" Copying from {from_file} to {to_file} \"")
print ("PRESS ENTER TO BEGIN PROCESS--->")
# We could do theese two on one line, how?
in_file = open(from_file)
indata = in_file.read()


input()

out_file = open(to_file, "w")
out_file.write(indata)

print("Alright all done.")
out_file.close()
in_file.close()