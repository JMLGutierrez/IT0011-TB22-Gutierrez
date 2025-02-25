#no exception handling for file not found immediate exit will occur
#Create a record management program given a list of students records. Each record must be a tuple consist of the following:
#
#Student ID: This must be a six digit number
#Student Name: Consist of first name and last name (you may set the fullname as tuple)
#Student Class Standing: The student class standing grade
#Major Exam Grade: Exam grade of the student

SID_list = []
FirstName_list = []
LastName_list = []
SClass_list = []
Major_list = []

choice = int
filename = ""

while choice != 9:
  print("\nSTUDENT DATABASE MANAGEMENT SYSTEM")
  print("--------------Menu----------------")
  print("[1]----------------------Open File")
  print("[2]----------------------Save File")
  print("[3]-------------------Save as File")
  print("[4]-------Show all Student Records")
  print("[5]------------Show Student Record")
  print("[6]---------------------Add Record")
  print("[7]--------------------Edit Record")
  print("[8]------------------Delete Record")
  print("[9]---------------------------Exit")

  choice = int(input("Enter your choice:"))

  if choice == 1:
      print("--------------------------------")
      filename = input("Enter the name of the file to open: ")

      if filename == "":
          print("No file name entered")
      else:
        f=open(filename + ".txt", "r") 
        print("File opened...\n")
        SID_list.clear()
        FirstName_list.clear()
        LastName_list.clear()
        SClass_list.clear()
        Major_list.clear()
        for line in f:
          data = line.strip().split(" ")
          if len(data) == 5:
            SID_list.append(data[0])
            FirstName_list.append(data[1])
            LastName_list.append(data[2])
            SClass_list.append(data[3])
            Major_list.append(data[4])
        

  elif choice == 2:
      print("--------------------------------")
      if filename == "":
          print("No file open\n")
      else:
          print("Saving File...")
          f=open(filename + ".txt", "a")
          for i in range(len(SID_list)):
            f.writelines(SID_list[i] + " " + FirstName_list[i] + " " + LastName_list[i] + " " + SClass_list[i] + " " + Major_list[i] + "\n")
          print("File saved...\n")

  elif choice == 3:
      print("--------------------------------")
      filename = input("Enter name of new record: ")
      with open(filename + ".txt", "w") as f:
          for i in range(len(SID_list)):
              f.writelines(SID_list[i] + " " + FirstName_list[i] + " " + LastName_list[i] + " " + SClass_list[i] + " " + Major_list[i] + "\n")

  elif choice == 4:
      print("--------------------------------")
      print("\nStudent Records:")
      if len(SID_list) == 0:
          print("NO RECORDS FOUND!\n")
      else:
          for i in range(len(SID_list)):
              print(f"\n----------{i + 1}----------")
              print(f"ID: {SID_list[i]}")
              print(f"Full Name: {LastName_list[i]}, {FirstName_list[i]}")
              print(f"Class Standing: {SClass_list[i]}")
              print(f"Major Exam Grade: {Major_list[i]}")

  elif choice == 5:
        print("--------------------------------")
        print("\nStudent Records Menu:")
        print("[1]-----------------By Last Name")
        print("[2]--------------------By Grades")

        shoice = int(input("Enter your choice: "))

        if len(SID_list) == 0:
            print("NO RECORDS FOUND!\n")

        elif shoice == 1:

            for i in range(len(LastName_list) - 1):
                for j in range(i + 1, len(LastName_list)):
                    if LastName_list[i] > LastName_list[j]:
                        LastName_list[i], LastName_list[j] = LastName_list[j], LastName_list[i]
                        FirstName_list[i], FirstName_list[j] = FirstName_list[j], FirstName_list[i]
                        SID_list[i], SID_list[j] = SID_list[j], SID_list[i]
                        SClass_list[i], SClass_list[j] = SClass_list[j], SClass_list[i]
                        Major_list[i], Major_list[j] = Major_list[j], Major_list[i]

            for i in range(len(LastName_list)):
                print(f"\n----------{i + 1}----------")
                print(f"ID: {SID_list[i]}")
                print(f"Full Name: {LastName_list[i]}, {FirstName_list[i]}")
                print(f"Class Standing: {SClass_list[i]}")
                print(f"Major Exam Grade: {Major_list[i]}")
                final_grade = (0.6 * float(SClass_list[i])) + (0.4 * float(Major_list[i]))
                print(f"Final Grade: {final_grade:.2f}")

        elif shoice == 2:
            final_grades = []
            for i in range(len(SID_list)):
                final_grade = ((0.6 * float(SClass_list[i])/300) + (0.4 * float(Major_list[i])/100))*100
                final_grades.append((final_grade, i))

            for i in range(len(final_grades) - 1):
                for j in range(i + 1, len(final_grades)):
                    if final_grades[i][0] < final_grades[j][0]:
                        final_grades[i], final_grades[j] = final_grades[j], final_grades[i]

            for index, (grade, i) in enumerate(final_grades):
                print(f"\n----------{i + 1}----------")
                print(f"ID: {SID_list[i]}")
                print(f"Full Name: {LastName_list[i]}, {FirstName_list[i]}")
                print(f"Class Standing: {SClass_list[i]}")
                print(f"Major Exam Grade: {Major_list[i]}")
                print(f"Final Grade: {grade:.2f}")

        else:
            print("Invalid choice!")


  elif choice == 6:
      choice2 = 'yes'
      while choice2.lower() == 'yes':
          print("--------------------------------")
          print("\nAdding Records :")
          good=False
          while good==False:
            s_id = input("Enter a Student ID: ")
            if len(s_id)==6:
              good=True
            else:
              print("Invalide ID")
           
          s_first_name = input("Enter Student First Name: ")
          s_last_name = input("Enter Student Last Name: ")
          while good==True:
            s_classSt = input("Student Class Standing [300]: ")
            if int(s_classSt)<=300:
              good=False
            else:
              print("Invalide Score")
          while good==False:
            s_major = input("Major Exam Grade[100]: ")
            if int(s_major)<=100:
              good=True
            else:
              print("Invalide Score")
            

          SID_list.append(s_id)
          FirstName_list.append(s_first_name)
          LastName_list.append(s_last_name)
          SClass_list.append(s_classSt)
          Major_list.append(s_major)

          choice2 = input("Do you want to enter another student? (yes/no): ")

  elif choice == 7:
      print("--------------------------------")
      print("\nEditing Record:")
      choice2 = 'yes'
      while choice2.lower() == 'yes':
          key = input("Enter Student ID to be changed: ")
          for i in range(len(SID_list)):
              if SID_list[i] == key:
                  SID_list[i] = input("Enter a Student ID: ")
                  FirstName_list[i] = input("Enter Student First Name: ")
                  LastName_list[i] = input("Enter Student Last Name: ")
                  SClass_list[i] = input("Student Class Standing: ")
                  Major_list[i] = input("Major Exam Grade: ")
          choice2 = input("Do you want to edit more? (yes/no): ")

  elif choice == 8:
      print("--------------------------------")
      print("\nDeleting Record:")
      choice2 = 'yes'
      while choice2.lower() == 'yes':
          key = input("Enter Student ID to delete record: ")
          for i in range(len(SID_list)):
              if SID_list[i] == key:
                  del SID_list[i]
                  del FirstName_list[i]
                  del LastName_list[i]
                  del SClass_list[i]
                  del Major_list[i]
                  break
          choice2 = input("Do you want to delete more? (yes/no): ")

  elif choice == 9:
      print("--------------------------------")
      print("|      Exit.....BYEEEEE        |")
      print("--------------------------------")

  else:
      print("Invalid Choice")
