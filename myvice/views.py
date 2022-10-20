from django.shortcuts import render##


def home(request):
	return render(request, 'home.html')###

def reverse(request):
	user_text = request.GET['usertext'] #встроенная функция реквеста - получение текста.  сам параметр получаем из окна ввода, в html
	reversed_text = user_text[::-1]
	count_element = len(user_text.split())
	print(count_element)
	return render(request, 'reverse.html', 
		{'usertext':user_text, 
		'reversedtext': reversed_text,
		'countelement': count_element})
