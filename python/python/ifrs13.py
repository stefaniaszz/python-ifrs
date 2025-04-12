Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())
naoAtendidos = 0
if Cr > Ca:
    naoAtendidos += (Cr - Ca)
if Br > Ba:
    naoAtendidos += (Br - Ba)
if Pr > Pa: 
    naoAtendidos += (Pr - Pa)
print(naoAtendidos)