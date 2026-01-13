while True:
    passwrd=input("enter the password(note:it must contain atleast 8 characters 1 uppercase 1 lower case 1 special character 1 number)")
    p=list(passwrd)
    upp=False
    low=False
    length=False
    num=False
    special=False
    if len(p)>=8:
     length=True  
    for ch in passwrd:
     if ch.isupper():
       upp= True
     elif ch.islower():
       low= True
     elif ch.isdigit():
       num=True 
     elif not ch.isalnum():
       special=True
    if upp and low and length:
       print("correct")
    if length==False:
      print("the length is less than 8 characters")
    if low==False:
      print("no lowercase")
    if num==False:
      print("no numbers")
    if upp==False:
      print("no upper case")
    if special==False:
      print("no special characters")
