from django.shortcuts import render, HttpResponse



def home_view(request):
    if request.user.is_authenticated:
        context={'name': 'Team'}
    else:
        context={'name': 'Guest User'}
   
    return render(request, 'home.html', context)

def menu_view(request):   
    return render(request, 'language/menu.html')

def menu_kr(request):   
    return render(request, 'language/menu_kr.html')

def menu_sp(request):   
    return render(request, 'language/menu_sp.html')

def menu_tk(request):   
    return render(request, 'language/menu_tk.html')


def phrases_view(request):   
    return render(request, 'language/phrases.html')

def phrases_kr(request):   
    return render(request, 'language/phrases_kr.html')

def phrases_sp(request):   
    return render(request, 'language/phrases_sp.html')

def phrases_tk(request):   
    return render(request, 'language/phrases_tk.html')

def test_view(request):   
    return render(request, 'language/Quiz.html')

def test_korean_view(request):   
    return render(request, 'language/ktest.html')

def test_turkish_view(request):   
    return render(request, 'language/ttest.html')

def test_english_view(request):   
    return render(request, 'language/etest.html')

def test_spanish_view(request):   
    return render(request, 'language/stest.html')

def test_result_view(request):   
    return render(request, 'language/test_result.html')

def ranking_view(request):   
    return render(request, 'language/ranking.html')