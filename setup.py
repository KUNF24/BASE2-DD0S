import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("apt install python3-pip")
    os.system("python -m pip install --upgrade pip")
    os.system("pip install requests")
    os.system("git pull")
    
elif c == "1":
    os.system("apt install python3-pip")
    os.system("python -m pip install --upgrade pip")
    os.system("pip3 install requests")
    os.system("git pull")
    print("Done.")
