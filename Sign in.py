#----------------------------------------------- بدايه مشروع تسجيل الطلاب -------------------------------
from os import *
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from functools import partial
#------------------------ برمجه الادوات -------------
def App () :
    def check_name (data):
        if len (data["name"]) <= 13 : # اصغر من او يساوي 13
            return ("name" , 'Plaese Write Full Name')
    
    
    popup ("Welcome Admin" , 
           put_text ("Dear Admin This Page It Is A Student Login System").onclick(lambda: toast("يجب عليك تسجيل جميع الطلاب المشتركين اولاً لتتمكن من معرفت جميع التفاصيل"))
    ) # رساله الترحيب
    put_html ('<center> <h2>Student Login System </h2> <img src ="https://th.bing.com/th?id=OIP.VM7a_vk4tHfO5Xu1rcH7MQHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2" width=120 ></center>')

    #------------------------------ الحقول لإدخال بيانات الطلاب -----------------
    
    data = input_group (
        "Add Student" ,
        [ 
         
         input ("Student Full Name : " , name = 'name'),
    
         input ("Student Email : " , name = 'email'),
         
         input ("Password Email : " , name = 'password' , type = PASSWORD ),
         
         input ("Age : " , name = 'age'),
         
         ] , validate = check_name  
    )
    # اظهار وجلب البيانات الي الموقع
    
    put_html ('<h2> New Student : </h2>').style('color:#0000ff;') 
    put_text ('User Name : %r' % data['name'])
    put_text ('Password : %r' % data['password'])
   
    
    
system('cls')    
#------------- امر تشغيل السيرفر -------------------
start_server(App , port=4567 , debug=True)


#start_server(هنا اسم الداله المطلوب تشغيلها و اظهارها , port=4567 , debug=True)
