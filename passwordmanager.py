import hashlib
import base64
from cryptography.fernet import Fernet

# def new_key():
#    key = Fernet.generate_key()
#    with open("cyphr.key","wb") as key_txt:   #    we already have key so no need for this
#      key_txt.write(key)

def load_key():
  cyphr=open("cyphr.key", "rb")
  key = cyphr.read()
  cyphr.close()
  return key

key=load_key()

og_pass=input("What is the password ? ").encode()

hashed_key = hashlib.sha256(key+og_pass).digest()


fer=Fernet(base64.urlsafe_b64encode(hashed_key))

try:
  
 with open("password.txt","r")as f:
   first_line=f.readline().rstrip()
   if first_line:
     user, passw = first_line.split("|")
     fer.decrypt(passw.encode())
except FileNotFoundError:
  pass # if the file doesn't exist , no passwords yet  ignore the program
except Exception:
  print("Wrong Password!")
  exit()



def mode_add():
  user_name=input("Account Name : ")
  passwords=input("Password : ")

  with open('password.txt','a') as f:
    f.write(user_name + "|" + str(fer.encrypt(passwords.encode()).decode()) + "\n")
  

def mode_view():
 with open("password.txt","r") as f:
   for pwds in f.readlines():
     data = pwds.rstrip()
     user, passw = data.split("|")
     print("User:",user ,"|Password:",fer.decrypt(passw.encode()).decode())
  

while True:

 mode=input("\nwould you like to (add/view) passwords? type q to exit : \n").lower()

 if mode =="q":
    break
 if mode == "view":
  mode_view()
 
 elif mode == "add":
   mode_add()
 
 else:
   print("invalid mode!")