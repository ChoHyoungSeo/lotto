from django.shortcuts import render, redirect
import random

# Create your views here.
def home(request):
    return render(request, "home.html")

def result(request):
    # input number
    number_list= list()
    for i in range(0, 6):
        number = request.GET['number'+ str(i+1)] #get방식으로 갖고오는 거야
        # if num is null, redirect home.html
        if number == '':
            return redirect('home')
        number_list.append(int(number))

    #random number
    rand_list=list()
    for i in range(0, 7):
        rand = random.randrange(1, 46)
        #when rand in randlist (중복제거)
        while rand in rand_list:
            rand = random.randrange(1, 46)
        rand_list.append(rand)

    count = 0
    for i in range(0, 6):
        for j in range(0, 7):
            if number_list[i] == rand_list[j]:
                count += 1
    return render(request, 'result.html', {'number_list':number_list, 'rand_list':rand_list, 'count':count}) 

    #데이터가 넘어갈 때도 사용할 수 있도록 해주기 위해서