from tqdm import tqdm
import os
import time
local= time.asctime(time.localtime(time.time()))

import csv
data='data.csv'




def a():
    

                    global data1
                    global data

                    Id=input("| Enter ID Again To Check  : ")
                    with open(data,'r',encoding='utf')as f:
                        reader=csv.reader(f)
                        for row in reader:
                            if len(row)>0:
                                if Id==row[0]:
                                    print('\n | This ID IS Found ')
                                    a()


def An_NEW_ACCOUNT():
        
            #try:
                            
                print('\n----------------SIGN UP-----------------')
                print("\n\nWhat is your major ?")
                Major=input("Press [M] For Mangers , [S] For students , And [A] For othors : ")
                
                if Major == 'M' or Major=='m':#A1
                    
                    
                        
                        print('\n---------------------------------------')
                        while True:
                            Id=input('| Enter Your ID : ')
                            if not Id.isdigit():
                                print("\n| uncorrect ID. please enter a correct ID : ")
                                continue
                            else:
                                Id=int(Id)
                                break
                        a()    
                        print('---------------------------------------')
                        Name1 = input("| Enter Your Full Name : ")
                        print('---------------------------------------')
                        
                        
                        
                        while True:
                            Phone_Number =input("| Enter Your Phone Number : ")
                            if not Phone_Number.isdigit():
                                print('\n| uncorrect Input.try again : ')
                                continue
                            else:
                                Phone_Number=int(Phone_Number)
                                break
                    
                        print('---------------------------------------')
                        
                        Passowrd=input("| Enter your Passoword : ")
                        print('---------------------------------------')
                        Email=input('| Enter Your Email : ')
                        index=Email.index("@")
                        username=Email[:Email.index('@')]
                        
                        
                        print('---------------------------------------')
                        data1=[Id,Name1,Phone_Number,username,Passowrd]
                        with open(data,'a',encoding="utf-8")as f:
                                writer=csv.writer(f)
                                writer.writerows([data1])
                    
                    

                        n=10
                        while n >0:
                            if n==10:
                                print('\t Saving', end='')
                            
                            print(".",end='')
                            time.sleep(1/5)
                            n-=1
                            if n == 1:
                               main() 
                
                elif Major == 'S' or Major=='s':#A2
                    
                            
                        print('\n---------------------------------------')
                        while True:
                            Id=input('| Enter Your ID : ')
                            if not Id.isdigit():
                                print("\n| uncorrect ID. please enter a correct ID : ")
                                continue
                            else:
                                Id=int(Id)
                                break
                            
                        a()    
                            
                        print('---------------------------------------')
                        Name1 = input("| Enter Your Full Name : ")
                        print('---------------------------------------')
                        
                        
                        #DECTIONARY
                        while True:
                            Phone_Number =input("| Enter Your Phone Number : ")
                            if not Phone_Number.isdigit():
                                print('\n| uncorrect Input.try again : ')
                                continue
                            else:
                                Phone_Number=int(Phone_Number)
                                break
                        
                        print('---------------------------------------')
                        Passowrd=input("| Enter your Passoword : ")
                        print('---------------------------------------')
                        Email=input('| Enter Your Email : ')                   
                        index=Email.index("@")
                        username=Email[:Email.index('@')]
                        
                        print('---------------------------------------')
                        data1=[Id,Name1,Phone_Number,username,Passowrd]
                        with open(data,'a',encoding="utf-8")as f:
                                writer=csv.writer(f)
                                writer.writerows([data1])
                        
                        
                        
                        n=10
                        while n >0:
                            if n==10:
                                print('\t Saving', end='')
                            
                            print(".",end='')
                            time.sleep(1/5)
                            n-=1
                            if n == 1:
                               main()
        
                elif Major == 'A' or Major=='a':#A3
                    print('\n---------------------------------------')
                    while True:
                            Id=input('| Enter Your ID : ')
                            if not Id.isdigit():
                                print("\n| uncorrect ID. please enter a correct ID : ")
                                continue
                            else:
                                Id=int(Id)
                                break
                    a()
                    print('---------------------------------------')
                    Name1 = input("| Enter Your Full Name : ")
                    print('---------------------------------------')
                    #DECTIONARY
                    while True:
                         Phone_Number =input("| Enter Your Phone Number : ")
                         if not Phone_Number.isdigit():
                                print('\n| uncorrect Input.try again : ')
                                continue
                         else:
                                Phone_Number=int(Phone_Number)
                                break
                    print('---------------------------------------')
                    Passowrd=input("| Enter your Passoword : ")
                    print('---------------------------------------')
                    Email=input('| Enter Your Email : ')                                  
                    index=Email.index("@")
                    username=Email[:Email.index('@')]
                    
                    print('---------------------------------------')
                    data1=[Id,Name1,Phone_Number,username,Passowrd]
                    with open(data,'a',encoding="utf-8")as f:
                            writer=csv.writer(f)
                            writer.writerows([data1])
                    
                    

                    
                    n=10
                    while n >0:
                        if n==10:
                            print('\t Saving', end='')
                        
                        print(".",end='')
                        time.sleep(1/5)
                        n-=1
                        if n == 1:
                           main()
                     
                    
            #except:
                #print("check your phone number")
    
def An_old_account():
        
         

                    global data1
                    global data
                    print("\n----------------LOG IN----------------------")
                    Id=input("Enter ID  : ")
                    with open(data,'r',encoding='utf')as f:
                        reader=csv.reader(f)
                        for row in reader:
                            if len(row)>0:
                                if Id==row[0]:
        
                                     password =row[4]
             
                                     word =""
                                     count = 0
                                     limit = 3
                                     out = False 
                                     while word != password and not (out):#BA
                                         if count < limit :#BA1
                                                word  = input("Enter the password of your account : ")
                                                count +=1
                                         else:#BA2
                                             out = True
                                     if out:#BA|1
                                         print ("out of try")
                                     else:#BA|2
                                        print('                            ###############################################')
                                        print("                            #       welcome to your account               #")
                                        print('                            ###############################################\n\n')
                                        print("_________________  ________________  __________________")
                                        print("|For leasing [1]|  |For renting[2]|  |For selling [3] |")
                                        print("^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^")
                                        a=int(input("please enter your choice :  "))
                                        
                                        
                                        
                                        if a==1:#BA|2|1
                                            print("what kind of rooms or apartements do you want to leas?\n")
                                            lista={1:'old room',2:'new room',3:'old apartemen',4:'new apartment',5:'old bulding',6:'new bulding',7:'old shop',8:'new shop'}
                                            print (lista)
                                            q=int(input("please enter the number of your choice .Next step=0 :"))
                                            w=lista[q]
                                            price=float(input('Enter the price : '))
                            
                                            while q in lista:
                                                if q==0:
                                                     main()
                                                w=lista[q]

                                                print('*******************************************************')
                                                print('* THE TIME:',local)
                                                print('*******************************************************')
                                                print('* Your choice is :',w,'\n it cost :',price,'RY')
                                                print('*******************************************************')
                                                q=int(input("please enter the number of your choice .Next step=0.  "))
                                                    
                                                if q==0:
                                                    main()

                                                price=float(input('Enter the price : '))
                                                n=open(f'{Id}.txt','a')
                                                n.write(w)
                                                n.close()
                                                
                                                 
                                        
                                        elif a==2:
                                              print('                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                                              print('                             ^      Welcome to rent places          ^')
                                              print('                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n')
                                              
                                              
                                              
                                                
                                              try:

                                                s=1
                                                while s:
                                                    listb={1:'old room',2:'new room',3:'old apartemen',4:'new apartment',
                                                           5:'old bulding',6:'new bulding',7:'old shop',8:'new shop'}
                                                    print(listb)
                                                    choice=int(input('Please enter your choice for skip press[0]: '))
                                                    b=choice
                                                    r=listb[choice]
                                                    place=input('Enter your place which you want to rent : ')
                                                    print('\n')
                                                    WA={'oldroom':20000,'newroom':35000,'oldapartment': 60000,'newapartment': 80000,
                                                        'oldbulding':200000,'newbulding':300000,'oldshop':40000,'newshop':70000}
                                                     
                                                    n=open(f'{Id}.txt','a')
                                                    n.write(r)
                                                    n.write('\n'+place)
                                                    n.close()
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    if choice==1:
                                                        print('  #########################################################')
                                                        print('  #  your choice is ',r,'. It cost is ',WA['oldroom'],'RY','     # ')                  
                                                        print('  #  your place is ',place             ,'')
                                                        print('  # THE TIME:',local)
                                                        print('  #########################################################\n\n')
                                                      
                                                        
                                                    
                                                    elif choice==2:
                                                        print('  #########################################################')
                                                        print('  #  your choice is ',r,'. It cost is ',WA['newroom'],'RY','     # ')                  
                                                        print('  #  your place is ',place             ,'')
                                                        print('  # THE TIME:',local)
                                                        print('  #########################################################\n\n')
                                                        
                                                    elif choice==3:
                                                        print('  #########################################################')
                                                        print('  #  your choice is ',r,'. It cost is ',WA['oldapartment'],'RY','     # ')                  
                                                        print('  #  your place is ',place             ,'')
                                                        print('  # THE TIME:',local)
                                                        print('  #########################################################\n\n')
                                                    elif choice==4:
                                                        print('  #########################################################')
                                                        print('  #  your choice is ',r,'. It cost is ',WA['newapartment'],'RY','     # ')                  
                                                        print('  #  your place is ',place             ,'')
                                                        print('  # THE TIME:',local)
                                                        print('  #########################################################\n\n')
                                                    elif choice==5:
                                                        print('  #########################################################')
                                                        print('  #  your choice is ',r,'. It cost is ',WA['oldbulding'],'RY','     # ')                  
                                                        print('  #  your place is ',place             ,'')
                                                        print('  # THE TIME:',local)
                                                        print('  #########################################################\n\n')
                                                    elif choice==6:
                                                        print('  #########################################################')
                                                        print('  #  your choice is ',r,'. It cost is ',WA['newbulding'],'RY','     # ')                  
                                                        print('  #  your place is ',place             ,'')
                                                        print('  # THE TIME:',local)
                                                        print('  #########################################################\n\n')
                                                    elif choice==7:
                                                        print('  #########################################################')
                                                        print('  #  your choice is ',r,'. It cost is ',WA['oldshop'],'RY','     # ')                  
                                                        print('  #  your place is ',place             ,'')
                                                        print('  # THE TIME:',local)
                                                        print('  #########################################################\n\n')
                                                    elif choice==8:
                                                        print('  #########################################################')
                                                        print('  #  your choice is ',r,'. It cost is ',WA['newshop'],'RY','     # ')                  
                                                        print('  #  your place is ',place             ,'')
                                                        print('  # THE TIME:',local)
                                                        print('  #########################################################\n\n')
                                                    
                                                            

                                              except:
                                                  main()
                        #                                print('                      ************************************************')
                        #                                print('                      *    Your choice is false. please try again.   *')
                        #                                print('                      ************************************************')
                        #     


                                                 
                                        elif a==3:
                                            print("what kind of rooms or apartements do you want to sell?\n")
                                            lista={1:'old room',2:'new room',3:'old apartemen',4:'new apartment',5:'old bulding',6:'new bulding',7:'old shop',8:'new shop'}
                                            print (lista)
                                            q=int(input("please enter the number of your choice .Next step=0 :"))
                                            
                                            a=lista[q]
                                            price=float(input('Enter the price : '))
                            
                                            while q in lista:
                                                if q==0:
                                                     break
                                                a=lista[q]
                                                n=open(f'{Id}.txt','a')
                                                n.write(w)
                                                n.close()
                                                
                                                print('*******************************************************')
                                                print('* THE TIME:',local)
                                                print('*******************************************************')
                                                print('* Your choice is :',a,'\n it cost :',price,'RY')
                                                print('*******************************************************')
                                                q=int(input("please enter the number of your choice .Next step=0.  "))
                                            
                                                if q==0:
                                                    break
                                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                                price=float(input('| Enter the price : '))
                                                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                                                n=open(f'{Id}.txt','a')
                                                n.write(w)
                                                n.close()
                                    ###################
                                     break
                            else:
                                print("ID is not found in our database!!")
                    input("press any keys to continue.......")   

                         
                         
def Edit_information():
    global data
    print("-------------update record-----------------------")
    Id=input("Enter your ID to update : ")
    idx_employee=None
    update_rec=[]
    with open(data,'r',encoding='utf-8')as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
           if len(row)>0:
                if Id==row[0]:
                    idx_employee=counter
                    print(" ID found :at index",idx_employee)
                    employee_data=[]
                    lis=['ID','Name    ','Phone Number','Email    ','  Passowrd']
                    for field in lis:
                         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                         value=input("| Enter Your  "+field+" : ")
                         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                         employee_data.append(value)
                    update_rec.append(employee_data)
                else:
                    update_rec.append(row)
                counter+=1
        if idx_employee is not None:
            with open(data,'w',encoding='utf-8')as f:
                writer=csv.writer(f)
                writer.writerows(update_rec)
        else:
            print("                    ID is not found in our database!!!")
            print("             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        input("press any key to continue..........")
        main()
                         
def display():
    password ='awa'
                 
    word =""
    count = 0
    limit = 3
    out = False 
    while word != password and not (out):#BA
          if count < limit :#BA1
             word  = input("Enter the password if you are manger : ")
             count +=1
          else:
             out = True
    if out:
        print ("out of try")
        

    
    global data
    print("------------------------------ID RECORD--------------------------------------")
    with open(data,'r',encoding='utf-8')as f:
        reader=csv.reader(f)
        lis=['ID','Name    ','Phone Number','Email    ','   Passowrd']
        for k in lis:
            print(k,end='\t | ')
        print("\n---------------------------------------------------------------------------------")
        for row in reader:
            print('\n')
            for item in row:
                print(item,end='\t | ')

        print("\n")
    input("press any key to continue")
    main()
    
                         
                         
                         
def search():
    global data
    print("----------------SEARCH----------------------")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    Id=input("|Enter ID that you search it : ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    with open(data,'r',encoding='utf')as f:
        reader=csv.reader(f)
        
        for row in reader:
            if len(row)>0:
                if Id==row[0]:
                    print("----------ID found-----------\n")
                    print("-----------------------------------")
                    print("| ID : ",row[0])
                    print("-----------------------------------")
                    print("| Name : ",row[1])
                    print("-----------------------------------")
                    print("| Phone : ",row[2])
                    print("-----------------------------------")
                    print("| Email : ",row[3])
                    print("-----------------------------------")
                    print("| password : ",row[4])
                    print("-----------------------------------")
                    try:
                        
                        c=open(f'{Id}.txt','r')
                        v=c.readlines()
                        print('| ROOM  : '+v[0])
                        print("-----------------------------------")
                        print('| place  : '+v[1])
                        print("-----------------------------------")
                        input('Press any key to go to the menu.........')
                        main()
                        break
                    except:
                        pass
                    
                else:
                           print("ID is not found in our database!!")
                         
                         
                         
def delete():
    
    global data
    print("------------------------------------------------")
    Id= input("{ Enter ID that you want to delete it : ")
    print("------------------------------------------------")
    
    employee_locate=False
    update_rec=[]
    
    with open (data,'r',encoding='utf-8') as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0:
                if Id !=row[0]:
                    update_rec.append(row)
                    counter+=1
                else:
                    employee_locate=True
    if employee_locate is True:
        with open (data,'w',encoding='utf-8') as f:
            writer=csv.writer(f)
            writer.writerows(update_rec)
        print("Id :.",Id,' delete successfully')
    else:
        print('Id  not found in our database')
    input("press any key to continue")
    main()

                         
                         

                         
                           
def main():
    import time
    
    
    local= time.asctime(time.localtime(time.time()))
    print('\n        *************************************************')
    print('        *      \tTHE TIME:',local,'     *')
    print('        *************************************************')
    print("\n")
    print('     --------------------------------------------')
    print('''    |      FOR CREATING AN ACCOUNT      [1]     |
    |      TO ENTER IN YOUR ACCOUNT     [2]     |
    |      TO EDIT YOUR INFORMATION     [3]     |
    |      TO LOOK FOR YOUR INFORMATION [4]     |
    |      TO SHOW ALL INFORMATION      [5]     |
    |      TO DELETE ACCOUNT            [6]     |
    |      TO QUIT                      [7]     |''')
    print('     --------------------------------------------\n')
    x=int(input("ENTER THE NUMBER FROM LIST HERE : "))
    print('\n')
    
    
    if x==1:
        print('      Loading...')
        for i in tqdm(range(100)):
            
         time.sleep(0.01)
        
        An_NEW_ACCOUNT()
        
       


        os.system('cls')
    elif x==2:
        print('      Loading...')
        for i in tqdm(range(100)):
            
         time.sleep(0.01)
        An_old_account()
    elif x==3:
        print('      Loading...')
        for i in tqdm(range(100)):
            
         time.sleep(0.01)
        Edit_information()
    elif x==4:
        print('      Loading...')
        
        for i in tqdm(range(100)):
            
         time.sleep(0.01)
        search()
    elif x==5:
        print('      Loading...')
        for i in tqdm(range(100)):
            
         time.sleep(0.01)
        display()
    elif x==6:
        print('      Loading...')
        for i in tqdm(range(100)):
             
          time.sleep(0.01)
        delete()
    else:
        print('--------------------------------------T H A N C K S--------------------------------------')
        
        


import pyfiglet


print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print(pyfiglet.figlet_format("RENT ROOM APP",font='slant',justify="center"))
print('|||| Design By\\Abdulrahman Hamoud AL-Atabi And Wajdy Nasser AL-Ajam          |||')
print('|||| Under The Supervision of Eng\\Mohammed AL-Souti And Eng\Mansour AL-Saidi |||')
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")

print('      Loading...')
for i in tqdm(range(100)):
    
        
    time.sleep(0.00001)

while True:     
   main()  

 
 








