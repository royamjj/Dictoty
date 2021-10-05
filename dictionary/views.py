from django.shortcuts import redirect, render
from PyDictionary import PyDictionary


def index(request):
    output = {}
    output['Noun'] = 'None'
    output['Verb'] = 'None'
    output['Adjective'] = 'None'
    if request.method == 'POST':
        word = request.POST.get('search')
        if word != None:
            dictionary = PyDictionary()
            meaning = dictionary.meaning(word)
            output['Noun'] = ', '.join(meaning.get('Noun', ['None']))
            output['Verb'] = ', '.join(meaning.get('Verb', ['None']))
            output['Adjective'] =', '.join( meaning.get('Adjective', ['None']))
        render(request, 'dictionary/word.html',output)
    return render(request, 'dictionary/word.html',output)
