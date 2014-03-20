from django.shortcuts import render



def record_detail(request):
    return render(request, 'blog/record_detail.html', {
        'form': form})
