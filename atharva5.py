import csv
def write_csv(general_info_list):
    with open("student_info.csv","a",newline="") as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["NAME","AGE","CONTACT NO.","EMAIL-ID","GENDER"])
        writer .writerow(general_info_list)
if __name__=="__main__":

  condition=True
  while(condition):
    student_info=input("Enter Name Age Contact No. Email-id Gender")
    print("Entered information:"+ student_info)
    student_info_list=student_info.split(" ")
    print("Entered split up information:"+ str(student_info_list))
    write_csv(student_info_list)
    choice_check=input("Enter yes/no if entered information is correct")
    if choice_check =="yes":
      write_csv(student_info_list)
      condition_check =input("Enter yes/no to enter other student information")
      if condition_check=="yes":
          condition=True
      elif condition_check=="no":
          condition=False
    elif choice_check=="no":
        print("enter the values again")   