from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">我的第一个网页</h1>'
    line3 = '<hr>'
    line2 = '<img style="max-width:100%;overflow:hidden;" src="https://s.cn.bing.net/th?id=OHR.HonaunauNP_ZH-CN4491662962_UHD.jpg&rf=LaDigue_UHD.jpg&w=3840&h=2160&c=8&rs=1&o=3&r=0">'
    return HttpResponse(line1 + line3 + line2)
