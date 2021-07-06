from django.shortcuts import render
from nltk.corpus import wordnet

# Create your views here.
def part(request):
    if request.method == 'POST':
        w = request.POST.get('mot', None)
        correct = True
        try:
            a = str(wordnet.synsets(w)[0])
            if w[0] != request.sesson["lettre"]:
                correct = False
            else:
                request.session['mot_trouve'] += 1
        except IndexError:
            correct = False
            data = {
                'mot': w, 'correct': correct,
            }
    else:
        return render(request, 'part1.html')