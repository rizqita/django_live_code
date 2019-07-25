from django.shortcuts import render,redirect
from .models import Barang
from .forms import inputBarang
# Create your views here.
def main_page(request):
    list_barang = Barang.objects.all()
    return render(request,'index.html',{'list_barang':list_barang})
def input_barang(request):
    if request.method == "POST":
        form = inputBarang(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('http://127.0.0.1:8000/input_barang')
    else:
        form = inputBarang()
    return render(request,'input_barang.html',{'form':form})
def barang_detail(request,barang_id):
    try:
        list_barang = Barang.objects.get(pk=barang_id)
    except Barang.DoesNotExist:
        raise Http404("Barang tidak ada")
    return render(request,'detail_barang.html',{'list_barang':list_barang})