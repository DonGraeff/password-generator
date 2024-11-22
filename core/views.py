import random
import string
from django.shortcuts import render

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def generate_password_view(request):
    password = ''
    if request.method == 'POST':
        try:
            length = int(request.POST.get('length', 8))
        except ValueError:
            length = 8

        use_uppercase = 'uppercase' in request.POST
        use_numbers = 'numbers' in request.POST
        use_special_chars = 'special' in request.POST
        
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    
    return render(request, 'index.html', {'password': password})
