import os
import pyfiglet
from subprocess import check_output
from colorama import Fore , Back
from colorama.initialise import init
p = 3

init ()

print (Fore.LIGHTYELLOW_EX)

print(pyfiglet.figlet_format("F O R M A T"))

print(Fore.RED)

print(pyfiglet.figlet_format("F I N D E R"))

while p : 
 init ()

 print ("\n"+Fore.GREEN + "Enter the desired location for the search")
 print (Fore.WHITE)
 location = input ()

 c = os.chdir(location)
 
 print (Fore.GREEN + "What format do you want to find ? ")
 
 print (Fore.WHITE)

 formatt = input ()

 if "." in formatt:
   None
 else:
       a ="."+formatt
 
 r="123"
 
 r = check_output("dir /S /B *" + formatt , shell=True).decode()
 
 i=r.replace(" ", "^").split()
 
 iba=i
 
 w= 0

 for s in i:
    s=s.replace("^"," ")
    w+=1
    
    ll=str(w)
    
    a = (len(s)+len(ll))

    a+=5

    print (Fore.LIGHTYELLOW_EX + a * "-")
    
    print (Fore.BLUE +"[" + ll + "] : "+Fore.RED+ s)

    print ("\n")
 
 while 1>0 :
  print (Fore.YELLOW +"[1]"+ Fore.RED + " exit\n" + Fore.YELLOW +"\n[2]" + Fore.BLUE + " continue\n" + Fore.YELLOW + "\n[3]" + Fore.LIGHTRED_EX + " delet file\n")
 
  print (Fore.GREEN + "chose option : ")

  print (Fore.WHITE)
 
  ent = input ()
 
  if ent == "1":
     os.system("cls")
     exit()
  elif ent == "2":
       os.system("cls")
       break
  elif ent == "3" :
      while 1>0:
       print (Fore.GREEN+"How do you delete files?\n")
       print (Fore.YELLOW+"[1]"+Fore.LIGHTMAGENTA_EX +" Select a one file for delete \n")
       print (Fore.YELLOW+"[2]"+Fore.LIGHTCYAN_EX +" Remove from x to y \n")
       print (Fore.GREEN+"Select an option to continue : \n ")
       print(Fore.WHITE)
       ent = input()
       r=r.split(".ghg")
       if ent == "1" :
         while 1 > 0:
          print(Fore.RED + "chose number for delet ") 
          print (Fore.WHITE)
          num = input()

          num = int(num)

          num = num -1

         

          os.system ("del "+'"'+iba[num].replace("\n","").replace("\r","").replace("^"," ") +'"')
          
          print ("\n"+Fore.YELLOW + "file " + Fore.LIGHTBLUE_EX + '"' + iba[num].replace("\n","").replace("\r","").replace("^"," ") + "." + formatt + '"' + Fore.RED + " was deleted")

          input ("\npress any key to continue")
            
          os.system("cls")

          r = check_output("dir /S /B *" + formatt , shell=True).decode()
          
          i=r.replace(" ", "^").split()
          iba=i

          w= 0

          for s in i:
              s=s.replace("^"," ")
              w+=1
    
              ll=str(w)
    
              a = (len(s)+len(ll))

              a+=5

              print (Fore.LIGHTYELLOW_EX + a * "-")
    
              print (Fore.BLUE +"[" + ll + "] : "+Fore.RED+ s)

              print ("\n")
            
          print("\n"+Fore.YELLOW + "[1] " + Fore.LIGHTRED_EX + "Delete another file")
          print ("\n"+Fore.YELLOW + "[2] " + Fore.LIGHTBLUE_EX + "Change the delete method") 
          print ("\n"+Fore.YELLOW +"[3] " + Fore.RED + "exit")
          print("\n"+Fore.GREEN+"chose number : ")
          ent1 = 0
          ent1=input()
          ent1 = int(ent1)
          if ent1 == 1 :
             print("ok")
          elif ent1 == 2:
             break
          elif ent1 == 3 :
             exit()
       else :
         while 1 > 0 :
           print (Fore.LIGHTRED_EX+"chose x number  ")
           print(Fore.WHITE)
           num = input()
           print(Fore.LIGHTBLUE_EX+"chose y number ")
           print(Fore.WHITE)
           num2= input()
           num2 = int(num2)
           num = int(num) -1

           for s in  range(num2):
     
               s= iba[num].replace("^"," ")
     
               os.system("del" + " "+ '"'+ s + '"')

               print( Fore.YELLOW + "file "+ Fore.LIGHTBLUE_EX + s +Fore.RED+ ' was deleted\n' )
     
               num += 1
           input("press any key to continue")

           os.system("cls")

           r = check_output("dir /S /B *" + formatt , shell=True).decode()
          
           i=r.replace(" ", "^").split()
           iba=i

           w= 0

           for s in i:
              s=s.replace("^"," ")
              w+=1
    
              ll=str(w)
    
              a = (len(s)+len(ll))

              a+=5

              print (Fore.LIGHTYELLOW_EX + a * "-")
    
              print (Fore.BLUE +"[" + ll + "] : "+Fore.RED+ s)

              print ("\n")
   
   
           print(Fore.YELLOW + "[1] " + Fore.LIGHTRED_EX + "Delete another file\n")
   
   
           print (Fore.YELLOW + "[2] " + Fore.LIGHTBLUE_EX + "Change the delete method\n") 
           print (Fore.YELLOW +"[3] " + Fore.RED + "exit\n")
           print(Fore.GREEN+"chose number : \n")
           print(Fore.WHITE)
           ent1 = 0
           ent1=input()
           ent1 = int(ent1)
           if ent1 == 1 :
            print(Fore.GREEN+"ok")
           elif ent1 == 2:
             break
           elif ent1 == 3 :
             exit()
            
 
  else :
     
       print (Fore.RED + "sory i cant find your number !!!\n")
     
       print (Fore.YELLOW +"press any key to exit")
     
       print (Fore.WHITE)
     
       input(": ")
     
       os.system("cls")
 
       exit()
 
    
input()
