#BMI_Calculator made by SANNIDHYA SAHOO,11191
name=(input("What is your name::"))
name=name.strip()
start=(input("Hi there. This is BMI Calculator.\nThis program is build on Python by Sannidhya Sahoo.\n ENTER 1 TO CONTINUE::"))
n=1
if start=='1':
    height=int(input('Enter your height (in cms)::'))
    weight=int(input('Enter your weight (in kgs)::'))
    BMI=weight/(height/100)**2
    print('\n\tYour BMI is',BMI)
    if BMI<18.5:
        print("\n\t＞︿＜",name," you are underweight.\n")
    elif BMI>=18.5 and BMI<25.0:
        print('\n\to*￣▽￣*o',name,', your weight is normal\n')
    elif BMI>=25 and BMI<30:
        print("\n\t＞﹏＜",name,", you are Overweight\n")
    elif BMI>=30 and BMI<35:
        print("\n\t⊙﹏⊙∥",name,", you are having Obesity (Class I)\n")
    elif BMI>=35 and BMI<40:
        print("\n\t{{{>_<}}}",name,",you are having Obesity (Class II)\n")
    elif BMI>=40:
        print("\n\t⊙_⊙;",name,", you are having Obesity (Class III)\n")
    else:
        print("INVALID INPUT(S) !!! .\nPROGRAM TERMINATED !!!")
ChoicOApp=int(input("\t^_^ Enter 2 if you would like to download \n\tBMI Calculator App for Android \n\tOr Enter 3 to view the source code \n\tENTER YOUR CHOICE::"))
import webbrowser
if  ChoicOApp==2:
    print("Opening Browser...")
    print("https://github.com/sannidhyasahoo/SensApp/raw/main/Sensors.apk")
    webbrowser.open("https://github.com/sannidhyasahoo/SensApp/raw/main/Sensors.apk")
elif ChoicOApp==3:
    print("Opening Browser...")
    print("https://github.com/sannidhyasahoo/BMI_Py/blob/main/BMI_Calculator.py") 
    webbrowser.open("https://github.com/sannidhyasahoo/BMI_Py/blob/main/BMI_Calculator.py")
print("if your browser doesn`t open copy the above\nlink and paste it on your browser")
print("========================================================================")
