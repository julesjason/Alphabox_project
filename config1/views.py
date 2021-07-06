from django.shortcuts import render


# Create your views here.
def config1(request):
    if request.method=='POST':
        level = request.POST['level']
        if level == "I":
            return render(request, 'part1.html')
        elif level == "II":
            return render(request, 'part1.html')

    else:
        return render(request, 'config1.html')

    return render(request, 'config1.html')