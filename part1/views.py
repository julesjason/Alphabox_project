from django.shortcuts import render

# Create your views here.
def part(request):
    return render(request, 'part1.html')