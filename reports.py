
# output with ReportLab/Platypus

from data_def import *

def meldungen_text(store):
    print "meldungen"
    for r in store.find(Rennen):
        print u"Rennen {r}".format(r=r.nr)
        for b in r.boote:
            print u"  Meldung {m}".format(m=b.team)


from reportlab.pdfgen import canvas

def meldungen_lowlevel(store):
    canv = canvas.Canvas('lowlevel.pdf')
    y = 750
    canv.drawString(50,y, "Meldungen")
    y -= 20
    for r in store.find(Rennen):
        if y < 100:
            canv.showPage()
            y=750
        canv.drawString(50,y, u"Rennen {r}".format(r=r.nr))
        y -= 12
        for b in r.boote:
            canv.drawString(50+20,y, u"Bug Nr. {nr}:".format(nr=b.bnr))
            canv.drawString(50+85,y, u"{m}".format(m=b.team))
            y -= 11
            if y < 50:
                canv.showPage()
                y=750
        y -= 5
    canv.showPage()
    canv.save()

def meldungen(store):
    meldungen_text(store)
    meldungen_lowlevel(store)

