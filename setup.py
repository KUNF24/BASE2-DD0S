import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("apt install python3-pip")
    os.system("apt-get install npm")
    os.system("npm install os")
    os.system("npm install sys")
    os.system("npm install threading")
    os.system("npm install string")
    os.system("git pull")
elif c == "1":
    os.system("apt install nodej-lts")
    os.system("apt install npm")
    os.system("npm i os")
    os.system("npm i sys")
    os.system("npm i threading")
    os.system("npm i string")
    os.system("git pull")
    print("Done.")
