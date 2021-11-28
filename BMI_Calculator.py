#BMI_Calculator made by SANNIDHYA SAHOO
start=(input("Hi There. This is BMI Calculator.\nThis program is build on Python by Sannidhya Sahoo.\n ENTER 1 TO CONTINUE :: "))
if start=='1':
          height=int(input('Enter your height (in cms)::'))
          weight=int(input('Enter your weight (in kgs)::'))
          BMI=weight/(height/100)**2
          print('Your BMI is',BMI)
          if BMI<18.5:
              print("You are underweight.")
          elif BMI>=18.5 and BMI<25.0:
              print('Your weight is normal')
          elif BMI>=25 and BMI<30:
              print("You are Overweight")
          elif BMI>=30 and BMI<35:
              print("You are having Obesity (Class I)")
          elif BMI>=35 and BMI<40:
              print("You are having Obesity (Class II)")
          elif BMI>=40:
              print("You are having Obesity (Class III)")
          else:
              print("INVALID INPUT(S) !!! .\nPROGRAM TERMINATED !!!")
ChoicOApp=int(input("Enter 2 if you would like to download \nBMI Calculator App \nOr Enter 3 to view the source code \nENTER YOUR CHOICE::"))
import webbrowser
if  ChoicOApp==2:
    print("Opening Browser...")
    print("Oprning https://github.com/sannidhyasahoo/SensApp/raw/main/Sensors.apk ...")
    webbrowser.open("https://github.com/sannidhyasahoo/SensApp/raw/main/Sensors.apk")
elif ChoicOApp==3:
    print("Opening Browser...")
    print("https://github.com/sannidhyasahoo/BMI_Py/blob/main/SourceCodeBMI_py")
    webbrowser.open("https://github.com/sannidhyasahoo/BMI_Py/blob/main/SourceCodeBMI_py")
