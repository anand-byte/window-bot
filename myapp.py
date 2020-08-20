import os

while True:    
       print("Hello Buddy! How can I help you:",end='')
       p=input()
       p=p.lower()
       if (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p))and (("chrome" in p) or ("browser" in p)):
          os.system("chrome")
       elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("notepad" in p) or ("editor" in p)):
          os.system("notepad")
       elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("player" in p) or ("video player" in p) or ("media player" in p) or ("music player" in p)):
          os.system("wmplayer")
       elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("mycomputer" in p) or ("my computer" in p) or ("file manager" in p) or ("explorer" in p) or ("file explorer" in p)):
          print("NOTE:This program can open C to F drive.")
          print("which drive do yo want me to open: ",end='')
          q=input()
          if q=='c' or q=='C':
            path = "C:/"
            path = os.path.realpath(path)
            os.startfile(path)
          elif q=='d' or q=='D':
            path = "D:/"
            path = os.path.realpath(path)
            os.startfile(path)
          elif q=='e' or q=='E':
            path = "E:/"
            path = os.path.realpath(path)
            os.startfile(path)
          elif q=='f' or q=='F':
            path = "F:/"
            path = os.path.realpath(path)
            os.startfile(path)
       elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("media player" in p) or ("video player" in p) or ("music player" in p)):
          os.system("wmplayer")
       elif (("exit" in p) or ("stop" in p) or ("terminate" in p)):
          print("Visit again!")
          break
       elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("pdf reader" in p) or ("reader" in p) or ("Adobe Reader" in p)):
          os.system("acroRd32")
       elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("excel" in p) or ("Excel" in p)):
          os.system("Excel")
       elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("power point" in p) or ("powerpoint" in p)):
          os.system("POWERPNT")
       elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("word" in p) or ("ms word" in p)):
          os.system("WINWORD")
       else:
          print("sorry! program not found.\nTry another way or install the program")