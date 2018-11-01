import json
import requests
from django.shortcuts import get_object_or_404, render

def login(request,token):
    res = requests.post(url='https://serene-wildwood-35121.herokuapp.com/oauth/getDetails', data={
    'token': token,
    'secret': 'ff5bbfae032e66f2abdb15b113bfab5d3f1741b1ed1f60b04e7062d74024bad29f57b82e6cfe0eee53ee6e595405c00907af0179c85c2c0c396e6e3df1f250a7'
})
    res = json.loads(res.content)
    email = res['student'][0]['Student_Email']
    #print(email)
    if(email):
        return render(request,'Hostel/login.html')
