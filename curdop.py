import os

z = 1
while(True):
    print("\n 1. Add Record")
    print("\n 2. Display all record")
    print("\n 3. Search student record by name ")
    print("\n 4. Search student record by rollno.")
    print("\n 5. Delete student record")
    print("\n 6. Update student record")
    print("\n 7. Exit\n")

    n = int(input("Enter your choice- "))
    if (n == 7):
       break
    elif (n == 1):
       print("Enter student details- ")
       n = input("Enter your name =  ")
       r = input("Enter your rollno. =  ")
       cl = input("Enter your class =  ")
       fees = input("Enter your fees =  ")
       per = input("Enter your percentage =  ")

       with open("developers.txt", 'a') as file:
          file.write(n + "-" + r + "-" + cl + "-" + fees + "-" + per + "\n")


    elif (n == 2):
        print("\n\nList of present records-\n\n")
        print("NAME-ROLLNO-CLASS-FEES-PERCENTAGE")

        with open("developers.txt", 'r') as file:
          while (True):
            d = file.readline()
            l = len(d)
            if (l == 0):
              break
            print(d.strip())
  

    elif (n==3):
        search_name = input("Enter student name- ")
        with open("developers.txt", 'r') as file:
         flag = 0
         while (True):
           t = file.readline()
           l = len(t)
           if (l == 0):
              break
           g = t.split('-')
           if(g[0] == search_name):
              print("\nRecord Found ")
              print("Name - ", g[0])
              print("Rollno. - ", g[1])
              print("Class - ", g[2])
              print("Fees - ", g[3])
              print("Percentage - ", g[4])
          
              flag = 1
              break

         if (flag == 0):
              print("\nRecord not found")
   
    elif (n==4):
        search_rollno = input("Enter student rollno.- ")
        with open("developers.txt", 'r') as file:
         flag = 0
         while (True):
           t = file.readline()
           l = len(t)
           if (l == 0):
              break
           g = t.split('-')
           if(g[1] == search_rollno):
              print("\nRecord Found ")
              print("Name - ", g[0])
              print("Rollno. - ", g[1])
              print("Class - ", g[2])
              print("Fees - ", g[3])
              print("Percentage - ", g[4])

              flag = 1
              break

         if (flag == 0):
              print("\nRecord not found")


    elif (n==5):
        search_name = input("Enter student name- ")
        with open("developers.txt", 'r') as file:
         with open("union.txt", 'w') as newfile:
          h = 0    
          flag = 0
          while (True):
            t = file.readline()
            l = len(t)
            if (l == 0):
              break
            g = t.split('-')
            if(g[0] != search_name):
              newfile.write(t)
            if(g[0] == search_name):
              h = 1
          if (h==1):
            print("Record deleted successfully")
            os.remove("developers.txt")
            os.rename("union.txt", "developers.txt")
          elif (h==0):
            print("Record not Found! deletion unsuccessful")
 

    elif (n==6):
       h = 0
       search_name = input("Enter student name- ")
       with open("developers.txt", 'r') as file:
          with open("union.txt",'w') as newfile:
           h = 0
           while (True):
             t = file.readline()
             l = len(t)
             if (l == 0):
               break
             g = t.split('-')
             if(g[0] == search_name):
               print("Current details are\n", t)
               print("--------------------")
              
               newroll = input("Want to change rollno ? Enter new details or press enter to continue ")
               newclass = input("Want to change class ? Enter new details or press enter to continue ") 
               newfees = input("Want to change fees ? Enter new details or press enter to continue ")
               newpercentage = input("Want to change percentage ? Enter new details or press enter to continue ")

               if (len(newroll) == 0):
                  newroll = g[1]
               if (len(newclass) == 0):
                  newclass = g[2]
               if (len(newfees) == 0):
                  newfees = g[3]
               if (len(newpercentage) == 0):
                  newpercentage = g[4]


               newfile.write("\n" + g[0] + "-" + newroll + "-" + newclass + "-" + newfees + "-" + newpercentage)

               h = 1
             else:
               newfile.write(t)
             if (h == 1):
               print("Record updated successfully")
               os.remove("developers.txt")
               os.rename("union.txt", "developers.txt")
             elif (h==0):
               print("No Such Record Exist: For Updation Process")
