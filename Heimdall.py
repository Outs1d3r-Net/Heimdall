from progress.bar import Bar
from datetime import *
import requests
import platform
import sys
import os

if 'Win' in platform.system():
    cls = os.system('cls')

else:
    cls = os.system('clear')

cls

if len(sys.argv) != 3:
    print("#"*42)
    print("\t\b\b\bHEIMDALL v.2.0 by: Outs1d3r-Net")
    print("#"*42)
    print('''
MMMMMMMMM0kWMk;dNWo,;,:oNNOkd0WMMMMMMO
MMMMMMMMM,NMM:dMModOcKoc;cXMWllMMMMMMO
MMMMWMMMMkkMMdxMMcW,O,.oNd xMMNMMWMMMO
MMMMWMMMMWdMM0kMM:o.;,dMOlOxlMMMWMMMMO
MMMMMWMMMMOMMNXMMN0xl,.':WMMklMMWMMMMO
MMMMMMWMMMMMMMMMMMMMMMWk';WMX:OWMMMMMO
MMMMMMWMMMMMMMMMMMMMMMMMM:lNcx,MMMMMMO
MMMMoXMWMMMMMMMMMMMMMMMMMO.0ox.WMMMMMO
MMMW.lMMWMMk0MNo0MMMMMMMM:.OMo.WMMMMMO
MMMx .WMWMW.;WM0.0MMMMMMl.:NN.:MMMMMMO
MMM,',OMMWM.l.o,.,dXMMMX.c,k, 0MMMMMMO
MMX''o;MMMWX;o...;c.0MMk l0,. :dMMMMMO
MM0' :;MMMWM,.k.xdd,,Wx.,.. c;'lMMMMMO
MMMo..NMMMMWo ,.''ol;..'l0O.. ,.XMMMMO
MMMc.'MMMMMN. .ol:;d';.NMWW;. .,lMMMMO
MMMx'.MMMMMW. ::'olo;.:kXd. '  ':MMMMO
MMMk..MMMMMM: . .o x..c  '  .  ,NMMMMO
MMMdo.MMMMMM' . ;:;o ;..,.   .'NMMMMMO
MMMll.MMMMMW;   . .  .c'    .oWMMMMMMO
MMO.,,lWMMK. '...' .'     ..'MMMMMMMMO
MM;.;X.OMMc'.    .' :.     . NMMMMMMMO
MM,... .xk:  ,    ; o      ' dMMMMMMMO
MMc.;  ,.',. ,.    '.    ; ..,MMMMMMMO
MMW';.  .. .  :    d.    '  ; WMMMMMMO
MMM:;lo .     c    ;,   .   l 0MMMMMMO
MMM:;oX     ' c    c.       l dMMMMMMO
''')
    print("Usage: python3",sys.argv[0],"TARGET.COM wordlist.txt\n")
    sys.exit(1)



print("#"*32)
print("[*]\tHEIMDALL v.2.0\t[*]")
print("#"*32)

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print("[+] Started... \t<",dt_string,"> [+]")
print('''
MMMMMMMMM0kWMk;dNWo,;,:oNNOkd0WMMMMMMO
MMMMMMMMM,NMM:dMModOcKoc;cXMWllMMMMMMO
MMMMWMMMMkkMMdxMMcW,O,.oNd xMMNMMWMMMO
MMMMWMMMMWdMM0kMM:o.;,dMOlOxlMMMWMMMMO
MMMMMWMMMMOMMNXMMN0xl,.':WMMklMMWMMMMO
MMMMMMWMMMMMMMMMMMMMMMWk';WMX:OWMMMMMO
MMMMMMWMMMMMMMMMMMMMMMMMM:lNcx,MMMMMMO
MMMMoXMWMMMMMMMMMMMMMMMMMO.0ox.WMMMMMO
MMMW.lMMWMMk0MNo0MMMMMMMM:.OMo.WMMMMMO
MMMx .WMWMW.;WM0.0MMMMMMl.:NN.:MMMMMMO
MMM,',OMMWM.l.o,.,dXMMMX.c,k, 0MMMMMMO
MMX''o;MMMWX;o...;c.0MMk l0,. :dMMMMMO
MM0' :;MMMWM,.k.xdd,,Wx.,.. c;'lMMMMMO
MMMo..NMMMMWo ,.''ol;..'l0O.. ,.XMMMMO
MMMc.'MMMMMN. .ol:;d';.NMWW;. .,lMMMMO
MMMx'.MMMMMW. ::'olo;.:kXd. '  ':MMMMO
MMMk..MMMMMM: . .o x..c  '  .  ,NMMMMO
MMMdo.MMMMMM' . ;:;o ;..,.   .'NMMMMMO
MMMll.MMMMMW;   . .  .c'    .oWMMMMMMO
MMO.,,lWMMK. '...' .'     ..'MMMMMMMMO
MM;.;X.OMMc'.    .' :.     . NMMMMMMMO
MM,... .xk:  ,    ; o      ' dMMMMMMMO
MMc.;  ,.',. ,.    '.    ; ..,MMMMMMMO
MMW';.  .. .  :    d.    '  ; WMMMMMMO
MMM:;lo .     c    ;,   .   l 0MMMMMMO
MMM:;oX     ' c    c.       l dMMMMMMO
''')

print("Set Target: [",str(sys.argv[1]),"]")
print("\n.\n\t\t\t\t\t\t\t\t\b\b[STATUS CODE]\t\t[HOST]\n")

subFOUND = []

f = open(str(sys.argv[2]), "r")

lenfile = open(str(sys.argv[2]),'r').read()
lenfile = len(lenfile.split())
bar = Bar('searching', max=int(lenfile))

for line in f:

    line = line.replace('\n', '')
    line = line.replace('!', '')
    line = line.replace('@', '')
    line = line.replace('#', '')
    line = line.replace('$', '')
    line = line.replace('%', '')
    line = line.replace('"', '')
    line = line.replace('&', '')
    line = line.replace('*', '')
    line = line.replace('(', '')
    line = line.replace(')', '')
    line = line.replace('[', '')
    line = line.replace(']', '')
    line = line.replace('{', '')
    line = line.replace('}', '')
    line = line.replace('^', '')
    line = line.replace('~', '')

    try:
        r = requests.head('http://'+line+'.'+str(sys.argv[1]))
        print('\t\t',r.status_code,'\t\t\thttp://'+str(line)+'.'+str(sys.argv[1]))
        subFOUND.append(line+'.'+str(sys.argv[1]))
    except UnicodeError:
        pass
    except UnicodeDecodeError:
        pass
    except requests.ConnectionError as exc:
        pass

    bar.next()

bar.finish()

print('\nShow Found: [\n')
for d in subFOUND:
    print(d)
print("\n].")
print('\n[-] End. \t</> [-]')

