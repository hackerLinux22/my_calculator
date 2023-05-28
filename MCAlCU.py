# my_calculator
import time
import sys
from colorama import *
import math
# یک حلقه کاملا تکراری
x=0
while(x==0) :
        time.sleep(2)
        # عملیات های مورد نظر و قابل انتخاب کاربر شامل 7 عمل ریاضی و غیره
        print(Fore.MAGENTA,"==========================================================")
        print(Fore.LIGHTRED_EX,"1.total        4.division        7.Abs        10.Other")
        print("                                                                       ")
        print(Fore.LIGHTRED_EX,"2.minus        5.power           8.sqrt")
        print("                                                                       ")
        print(Fore.LIGHTRED_EX,"3.zarb         6.Average         9.trigonometry")
        print(Fore.MAGENTA,"==========================================================")
        print("                                                                       ")
        # وارد کردن عملیات انتخاب شده
        a=input("Enter operation :")
        # مرحله جمع اعداد
        if(a=="total" or a=='1') :
                b=float(input("enter number one :"))
                c=float(input("enter number two :"))
                print(Fore.BLUE,"output :",b+c)
        # مرحله توان اعداد
        elif(a=="power" or a=='5') :
                b1=float(input("enter number :"))
                c1=float(input("enter power :"))
                print(Fore.BLUE,"output :",b1**c1)
        # مرحله تفریق اعداد
        elif(a=="minus" or a=='2') :
                b2=float(input("enter number one :"))
                c2=float(input("enter number two :"))
                print(Fore.BLUE,"output :",b2-c2)
        # مرحله میانگین اعداد
        elif(a=="Average" or a=='6') :
            # فقط تا پنج عدد درست است
                print("                           ")
                b3=int(input("number of numbers ?"))
                for n in range(0,b3) :
                        c3=int(input("Enter number :"))
                        c3+=c3
                        AVG=c3/b3
                print(Fore.BLUE,"average :",AVG)
        # مرحله ضرب اعداد
        elif(a=="zarb" or a=='3') :
                b4=float(input("enter number one :"))
                c4=float(input("enter number two :"))
                print(Fore.BLUE,"output :",b4*c4)
        # مرحله تقسیم اعداد
        elif(a=="division" or a=='4') :
                b5=float(input("enter number one :"))
                c5=float(input("enter number two :"))
                print(Fore.BLUE,"output :",b5/c5)
        # مرحله قدر مطلق اعداد
        elif(a=="Abs" or a=='7') :
                b6=float(input("enter number :"))
                num=b6
                print(abs(num))
        elif(a=="sqrt" or a=='8') :
            SQ=int(input("Enter number sqrt :"))
            SQO=math.sqrt(SQ)
            print(Fore.BLUE,"output :",SQO)
        elif(a=="trigonometry" or a=='9') :
            print(Fore.LIGHTGREEN_EX,"|    1.sin    2.cos    |")
            print(Fore.LIGHTGREEN_EX,"|                      |")
            print(Fore.LIGHTGREEN_EX,"|         3.tan        |")
            TR=input("Enter operation :")
            if(TR=="sin" or TR=='1') :
                SI=int(input("enter number angle :"))
                SIO=math.sin(SI)
                print(Fore.BLUE,"output :",SIO)
            elif(TR=="cos" or TR=='2') :
                CO=int(input("Enter number angle :"))
                COO=math.cos(CO)
                print(Fore.BLUE,"output :",COO)
            elif(TR=="tan" or TR=='3') :
                TA=int(input("Enter number angle :"))
                TAO=math.tan(TA)
                print(Fore.BLUE,"output :",TAO)
        # و عملیات های غیره
        elif(a=="other" or a=='10') :
                time.sleep(2)
                # مشاهده عملیات های غیره پروژه
                print("                                     ")
                print(Fore.CYAN,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print(Fore.WHITE,"1.Exit   2.Algorithm   3.information ")
                print(Fore.CYAN,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print("                                     ")
                # انتخاب کردن عملیات مورد نظر
                k=input("Enter operation :")
                if(k=="information" or k=='3') :
                    # در این عملیات اطلاعات پروژه نمایاین می شود
                    print(Fore.LIGHTMAGENTA_EX,"********************************************")
                    print(Fore.LIGHTMAGENTA_EX,"Fristname : Alireza       lastname : Mirzaei")
                    time.sleep(1)
                    print("                                            ")
                    print(Fore.LIGHTMAGENTA_EX,"Teachers : majid Khezri  and  Reza Ruhollah ")
                    time.sleep(1)
                    print("                                            ")
                    print(Fore.LIGHTMAGENTA_EX,"name project : my partner      class : 109  ")
                    print(Fore.LIGHTMAGENTA_EX,"********************************************")
                elif(k=="Algorithm" or k=='2') :
                    # دو مورد الگوریتم انتخابی توسط کاربر
                    print("                                               ")
                    print(Fore.YELLOW,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print(Fore.WHITE,"1.the largest number  or  2.the smallest number")
                    print(Fore.YELLOW,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    print("                                               ")
                    u=input("Enter optaions :")
                    if(u=='1') :
                        # الگوریتم اول
                        b7=float(input("enter number 1 :"))
                        c7=float(input("enter number 2 :"))
                        c8=float(input("enter number 3 :"))
                        if(b7>c7) :
                            if(b7>c8) :
                               print(Fore.BLUE,"big number :",b7)
                            else:
                               print(Fore.BLUE,"big number :",c8)
                        else:
                            if(c7>c8) :
                               print(Fore.BLUE,"big number :",c7)
                            else:
                               print(Fore.BLUE,"big number :",c8)
                    elif(u=='2') :
                        # الگوریتم دوم 
                        b8=float(input("enter number 1 :"))
                        b9=float(input("enter number 2 :"))
                        c9=float(input("enter number 2 :"))
                        if(b8<b9) :
                            if(b8<c9) :
                                print(Fore.RED,"small number :",b8)
                            else:
                                print(Fore.RED,"small number :",c9)
                        else:
                            if(b9<c9) :
                                print(Fore.RED,"small number :",b9)
                            else:
                                print(Fore.RED,"small number :",c9)
                elif (k == "Exit" or k == '1'):
                    # یک سوال از کاربر پرسیده می شود و کاربر با نوشتن yes یا no به آن پاسخ می دهد
                    o = input("Do you want to exit ?")
                    # در صورت نوشتن yes در مقابل جواب سوال کاربر برنامه بسته می شود
                    if (o == "yes"):
                          sys.exit("Goodbye")
