from django.shortcuts import render
from .models import Entry
from .forms import EntryForm 

# Create your views here.


def home(request):
	entries =Entry.objects.order_by('-post_date')
	context={ 'entries' : entries}
	return render(request, 'home.html', context)




def add(request):
	if request.method == 'POST':
		form = EntryForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form=EntryForm()	
	context = { 'form': form }
	return render (request, 'add.html', context)		
