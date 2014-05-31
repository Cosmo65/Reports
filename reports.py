
# output with ReportLab/Platypus

from data_def import *

def meldungen_text(store):
    print "meldungen"
    for r in store.find(Rennen):
        print u"Rennen {r}  ".format(r=r.nr), 
        for l in sorted(r.laeufe, key=lambda lauf: lauf.seq):
            print u"{t}{n}: {stz}, ".format(t=l.typ, n=l.seq, stz=l.startzeit),
        print
        for b in r.boote:
            print u"  Meldung {m}".format(m=b.team)


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def meldungen_lowlevel(store):
    canv = canvas.Canvas('lowlevel.pdf', pagesize=A4)
    Width,Height=A4
    y = Height - 50
    canv.drawString(50,y, "Meldungen")
    canv.line(50, y-2, Width-50, y-2)
    canv.line(50, y-4, Width-50, y-4)
    y -= 20
    for r in store.find(Rennen):
        if y < 100:
            canv.showPage()
            y=Height - 50
        canv.drawString(50,y, u"Rennen {r}".format(r=r.nr))
        y += 12
        for l in sorted(r.laeufe, key=lambda lauf: lauf.seq):
            y -= 12
            canv.drawString(250,y, u"{t}: {stz:%d.%m. %H:%M}".format(t=l.typ, stz=l.startzeit))

        canv.line(50, y-2, Width-50, y-2)
        y -= 12
        for b in r.boote:
            canv.drawString(50+20,y, u"Bug Nr. {nr}:".format(nr=b.bnr))
            canv.drawString(50+85,y, u"{m}".format(m=b.team))
            y -= 11
            if y < 50:
                canv.showPage()
                y=Height - 50
        y -= 5
    canv.showPage()
    canv.save()

def meldungen(store):
    meldungen_text(store)
    meldungen_lowlevel(store)

