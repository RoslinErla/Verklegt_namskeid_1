import os,time
os.system('clear')
filenames = ["ascii1.txt"]
frames = []

for name in filenames:
    with open(name,"r", encoding="utf8") as f:
        frames.append(f.readlines())

for frame in frames:
    print("".join(frame)) # sameinar allar línur í einn streng
    time.sleep(1)
    os.system('clear')