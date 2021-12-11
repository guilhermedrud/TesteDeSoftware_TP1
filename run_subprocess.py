import subprocess

f = open("input_test","r")
cp = subprocess.run(["python3","main.py"],stdin=f, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(cp)
f.close()