from django.shortcuts import render
import datetime

# Create your views here.
def templatedemo(request):
    date=datetime.datetime.now()
    name='manas'
    msg=''
    h=int(date.strftime('%H'))
    if h<12:
        msg=msg+' Good Morning... '
    elif h<16:
        msg=msg+' Good AfterNoon... '
    elif h<20:
        msg=msg+' Good Evening... '
    else:
        msg=msg+' Good Night'
    
    my_dict={'date':date,'name':name,'msg':msg}

    return render(request,'testapp/welcome.html',context=my_dict)
