import pandas as pd
import numpy as np
import string

data2 = pd.read_excel("data.xlsx") 
ff= open("output2.html","w+")
# print(data2)
phone  = data2.get("phone")  
state = data2.get("state")  
med = data2.get("med")  
add = data2.get("add") 





b = """
</body>
</html>

"""
dat = []
x=0
while x<len(data2):
    a="""<html>
<body> 
<doctypehtml{count}>""".format(count=x+1)


    new_phone = string.replace(str(phone[x]), '.', '&#39;')
    new_phone2 = string.replace(new_phone, '.', '&#39;')
    new_phone3 = string.replace(new_phone2, ':', '&#58;')
    new_phone4 = string.replace(new_phone3, ';', '&#59;')
    new_phone5 = string.replace(new_phone4, ',', '&#44;')
    new_phone6 = string.replace(new_phone5, '(', '&#40;')
    new_phone7 = string.replace(new_phone6, '/', '&#47;')
    new_phone8 = string.replace(new_phone7, '-', '&#45;')
    new_phone9 = string.replace(new_phone8, ')', '&#41;')


    new_state = string.replace(str(state[x]), '.', '&#39;')
    new_state2 = string.replace(new_state, '.', '&#39;')
    new_state3 = string.replace(new_state2, ':', '&#58;')
    new_state4 = string.replace(new_state3, ';', '&#59;')
    new_state5 = string.replace(new_state4, ',', '&#44;')
    new_state6 = string.replace(new_state5, '(', '&#40;')
    new_state7 = string.replace(new_state6, '/', '&#47;')
    new_state8 = string.replace(new_state7, '-', '&#45;')
    new_state9 = string.replace(new_state8, ')', '&#41;')




    new_med = string.replace(str(med[x]), '.', '&#39;')
    new_med2 = string.replace(new_med, '.', '&#39;')
    new_med3 = string.replace(new_med2, ':', '&#58;')
    new_med4 = string.replace(new_med3, ";", '&#59;')
    new_med5 = string.replace(new_med4, ',', '&#44;')
    new_med6 = string.replace(new_med5, '(', '&#40;')
    new_med7 = string.replace(new_med6, '/', '&#47;')
    new_med8 = string.replace(new_med7, '-', '&#45;')
    new_med9 = string.replace(new_med8, ')', '&#41;')


    new_add = string.replace(str(add[x]), '.', '&#39;')
    new_add2 = string.replace(new_add, '.', '&#39;')
    new_add3 = string.replace(new_add2, ':', '&#58;')
    new_add4 = string.replace(new_add3, ';', '&#59;')
    new_add5 = string.replace(new_add4, ',', '&#44;')
    new_add6 = string.replace(new_add5, '(', '&#40;')
    new_add7 = string.replace(new_add6, '/', '&#47;')
    new_add8 = string.replace(new_add7, '-', '&#45;')
    new_add9 = string.replace(new_add8, ')', '&#41;')



    z="""
    {phone}
    {state}
    {med}
    {add}""".format(phone=new_phone9, state=new_state9, med=new_med9, add=new_add9)
        
    dd= a+z+b
    ff.write(dd)
    dat.append(dd)
    print(dd)

    x+=1

# print(dat)


# print(a)