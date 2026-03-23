from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Talaba, Kitob, Muallif, Kutubxonachi, Record


def salom_view(request):
    return HttpResponse(
        """
        <h1 style="color:red;">Django MVT</h1>
        <hr>
        <p>Bugun django MVT o'rganamiz</p
        """
    )

def home_view(request):
    return render(request, "home.html")

def talabalar_view(request):
    talabalar = Talaba.objects.all()

    search=request.GET.get("search")
    if search:
        talabalar =talabalar.filter(ism__icontains=search)

    context = {
        "talabalar": talabalar,
        "search": search
    }
    return render(request, "talabalar.html", context)


def talaba_view(request,talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        "talaba": talaba
    }
    return render(request, "talaba.html", context)

def talaba_add_view(request):
    if request.method == "POST":
        ism=request.POST.get("ism")
        guruh=request.POST.get("guruh")
        kurs=request.POST.get("kurs")

        Talaba.objects.create(
            ism=ism,
            guruh=guruh,
            kurs=kurs
        )
        return redirect('/talabalar/')

    return render(request, "talaba_add.html")


def talaba_update_view(request, pk):
    talaba = Talaba.objects.get(id=pk)

    if request.method == "POST":
        talaba.guruh = request.POST.get("guruh")
        talaba.kurs = request.POST.get("kurs")

        talaba.save()
        return redirect("/talabalar/")

    return render(request, "talaba_update.html", {"talaba": talaba})



def talaba_delete_view(request,pk):
    talaba = Talaba.objects.get(id=pk)
    talaba.delete()
    return redirect('/talabalar/')


def talaba_delete_confirm_view(request,pk):
    talaba = Talaba.objects.get(id=pk)
    context = {
        "talaba": talaba
    }
    return render(request, "talaba_delete_confirm.html", context)


def kitoblar_view(request):
    kitoblar = Kitob.objects.all()

    q=request.GET.get("q")
    if q:
        kitoblar =kitoblar.filter(nom__icontains=q)

    ordering=request.GET.get("ordering","nom")
    kitoblar =kitoblar.order_by(ordering)


    context = {
        "kitoblar": kitoblar,
        "q": q,
        "ordering": ordering
    }
    return render(request, "kitoblar.html", context)

def kitob_view(request,kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {
        "kitob": kitob
    }
    return render(request, "kitob.html", context)

def kitob_add_view(request):
    mualliflar=Muallif.objects.all()

    if request.method == "POST":
        nom=request.POST.get("nom")
        janr=request.POST.get("janr")
        sahifa=request.POST.get("sahifa")
        muallif_id=request.POST.get("muallif")

        Kitob.objects.create(
            nom=nom,
            janr=janr,
            sahifa=sahifa,
            muallif_id=muallif_id
        )
        return redirect('/kitoblar/')

    return render(request, "kitob_add.html", {"mualliflar": mualliflar})

def kitob_update_view(request, pk):
    kitob = Kitob.objects.get(id=pk)
    mualliflar = Muallif.objects.all()

    if request.method == "POST":
        kitob.nom = request.POST.get("nom")
        kitob.janr = request.POST.get("janr")
        kitob.sahifa = request.POST.get("sahifa")
        kitob.muallif_id = request.POST.get("muallif")

        kitob.save()
        return redirect("/kitoblar/")

    return render(request, "kitob_update.html", {
        "kitob": kitob,
        "mualliflar": mualliflar
    })

def kitob_delete_view(request,pk):
    kitob = Kitob.objects.get(id=pk)
    kitob.delete()
    return redirect('/kitoblar/')


def kitob_delete_confirm_view(request,pk):
    kitob = Kitob.objects.get(id=pk)
    context = {
        "kitob": kitob
    }
    return render(request, "kitob_delete_confirm.html", context)


def mualliflar_view(request):
    mualliflar=Muallif.objects.all()
    context = {
        "mualliflar": mualliflar
    }
    return render(request, "mualliflar.html", context)

def muallif_view(request,muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    context = {
        "muallif": muallif
    }
    return render(request, "muallif.html", context)

def muallif_add_view(request):
    if request.method == "POST":
        ism=request.POST.get("ism")
        jins=request.POST.get("jins")

        Muallif.objects.create(
            ism=ism,
            jins=jins
        )
        return redirect('/mualliflar/')
    return render(request, "muallif_add.html")

def muallif_update_view(request, pk):
    muallif = Muallif.objects.get(id=pk)

    if request.method == "POST":
        muallif.ism = request.POST.get("ism")
        muallif.jins = request.POST.get("jins")

        muallif.save()
        return redirect("/mualliflar/")

    return render(request, "muallif_update.html", {"muallif": muallif})

def kutubxonachilar_view(request):
    kutubxonachilar=Kutubxonachi.objects.all()
    context = {
        "kutubxonachilar": kutubxonachilar
    }
    return render(request, "kutubxonachilar.html", context)

def kutubxonachi_view(request,kutubxonachi_id):
    kutubxonachi=Kutubxonachi.objects.get(id=kutubxonachi_id)
    context = {
        "kutubxonachi": kutubxonachi
    }
    return render(request, "kutubxonachi.html", context)

def kutubxonachi_add_view(request):
    if request.method == "POST":
        ism=request.POST.get("ism")
        ish_vaqti=request.POST.get("ish_vaqti")

        Kutubxonachi.objects.create(
            ism=ism,
            ish_vaqti=ish_vaqti
        )
        return redirect('/kutubxonachilar/')
    return render(request, "kutubxonachi_add.html")

def kutubxonachi_update_view(request, pk):
    kutubxonachi = Kutubxonachi.objects.get(id=pk)

    if request.method == "POST":
        kutubxonachi.ism=request.POST.get("ism")
        kutubxonachi.ish_vaqti=request.POST.get("ish_vaqti")

        kutubxonachi.save()
        return redirect('/kutubxonachilar/')
    return render(request, "kutubxonachi_update.html", {"kutubxonachi": kutubxonachi})

def recordlar_view(request):
    recordlar=Record.objects.all()
    context = {
        "recordlar": recordlar
    }
    return render(request, "recordlar.html", context)

def record_view(request,record_id):
    record = Record.objects.get(id=record_id)
    context = {
        "record": record
    }
    return render(request, "record.html", context)

def record_add_view(request):
    talabalar=Talaba.objects.all()
    kitoblar=Kitob.objects.all()
    kutubxonachilar=Kutubxonachi.objects.all()

    if request.method == "POST":
        talaba_id=request.POST.get("talaba")
        kitob_id=request.POST.get("kitob")
        kutubxonachi_id=request.POST.get("kutubxonachi")

        Record.objects.create(
            talaba_id=talaba_id,
            kitob_id=kitob_id,
            kutubxon_id=kutubxonachi_id,
        )
        return redirect('/recordlar/')
    return render(request, "record_add.html",{
        "talabalar": talabalar,
        "kitoblar": kitoblar,
        "kutubxonachilar": kutubxonachilar,
    })

def record_update_view(request, pk):
    record = Record.objects.get(id=pk)

    if request.method == "POST":
        record.qaytargan_vaqt=request.POST.get("qaytargan_vaqti")
        record.save()
        return redirect('/recordlar/')

    return render(request, "record_update.html", {"record": record})
