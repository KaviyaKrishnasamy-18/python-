class multiplefunctions():
    def oddeven():
        num=int(input("enter the number"))
        if((num%2)==1):
            print("odd number")
            message="odd number"
        else:
            print("even number")
            message="even number"
            return message 

    def BMI():
        BMI=int(input("enter the BMI index:"))
        if(BMI<18.5):
            print("underweight")
            message="underweight"
        elif(BMI<24.9):
            print("normal")
            message="normal"
        elif(BMI<29.9):
            print("overweight")
            message="overweight"
        else:
            print("very overweight")
            message="very overweight"
            return messages