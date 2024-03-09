# reading_writing_files.py

f = open("demofile.txt", "r")
print(f.read())

f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile.txt", "r")
print(f.read())