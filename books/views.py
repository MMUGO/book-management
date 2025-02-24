from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})

def reverse_string(s):
    stack = list(s)
    reversed_str = "".join(stack[::-1])
    return reversed_str

def reverse_string_view(request):
    reversed_text = None
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        reversed_text = reverse_string(input_text)
    return render(request, 'books/reverse_string.html', {'reversed_text': reversed_text})
