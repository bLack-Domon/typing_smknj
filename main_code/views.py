from django.shortcuts import render, redirect
from .models import TypingResult
from .forms import TypingResultForm

def leaderboard_view(request):
    putra = TypingResult.objects.filter(jenis_kelamin='L').order_by('-skor')
    putri = TypingResult.objects.filter(jenis_kelamin='P').order_by('-skor')
    return render(request, 'main.html', {'putra': putra, 'putri': putri})

def input_skor_view(request):
    if request.method == 'POST':
        form = TypingResultForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if 'screenshot' in request.FILES:
                uploaded_file = request.FILES['screenshot']
                nama = form.cleaned_data.get('nama', 'user').replace(' ', '_')
                skor = form.cleaned_data.get('skor', 0)
                ext = uploaded_file.name.split('.')[-1]
                new_filename = f"{nama}_{skor}.{ext}"
                uploaded_file.name = new_filename
                instance.screenshot = uploaded_file
            instance.save()
            return redirect('leaderboard')
    else:
        form = TypingResultForm()
    return render(request, 'skor.html', {'form': form})
