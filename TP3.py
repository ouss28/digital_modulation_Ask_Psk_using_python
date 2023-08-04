import numpy as np 
import matplotlib.pyplot as plt
import random as rd
#oumarouchi mohamed wassim 
def sine_wave(f,overSampRate,phase,nCyl,Amp=1):   #fonction sinus
    Amp1= 2
    Amp2 = 1
    fs = overSampRate*f
    t = np.arange(0,nCyl*1/f,1/fs)
    g = Amp*np.sin(2*np.pi*f*t+phase)
    return g,t
def argand(a,title):#fonction pour la visulation plan complex
    test = []
    for x in a:
        plt.polar([0,np.angle(x)],[0,abs(x)],marker='o',label='python')
        test.append("phi = {}, r = {}".format(np.round(np.angle(x),3),np.round(abs(x),3)))
    print(test)
    limit=np.max(np.ceil(np.absolute(a))) # set limits for axis
    plt.ylabel('Real')
    plt.xlabel('Imaginary')
    plt.title(title)
    plt.legend(['état:0', 'état:1'])
    plt.show()
def binary_sig(f,overSymple,nCyl):#fonction python générer séquence binaire
    # f: la fréquqnce 
    # il faut que overSymple > 2 selon shanon 
    fs = overSymple*f #fréquance échantillonnage
    bin_code =[rd.randint(0,1) for i in range(nCyl)] #sequence binaire pseudo aleatoire
    t = np.arange(0,nCyl/f,1/fs)
    sign = []
    for i in bin_code:
        for j in np.arange(0,1/f,1/fs):
            sign.append(i)
    return "".join([str(i)for i in bin_code]),sign
def modulation_ASk(sign,sin):
    return [(A1*sign[i]-A2*(sign[i]-1))*sin[i] for i in range(l)]
def modulation_PSK(t,f,phase,bin,Amp=1):   #fonction sinus
    return Amp*[np.sin(2*np.pi*f*t[i]+(phase[1]*bin[i]-phase[0]*(1-bin[i]))) for i in range(len(t))] # phi = phi2*i - ph1*(i-1) si i = 1 => phi = phi2 si i = 0 => phi = ph1
f = 20
A1 = 3 # pour le 1 
A2 = 1 # pour le 1 
# on a deux états
sin,t = sine_wave(f,30,0,10)
bin_code,seq_bin = binary_sig(f,30,10) 
l  =len(seq_bin)
ASK = modulation_ASk(seq_bin,sin)
# on a le meme phase donc on deux r = (si 1 => 3,si 0 => 1)
phi = [0,np.pi/4]
PSK = modulation_PSK(t,f,phi,seq_bin) 
# on a le meme Aumplited donc on deux r = (si 1 => 0,si 0 => pi)
ASK_complex = np.array([1,3]) + 1j*np.array([0,0])
# on a deux phases différent donc on utilise la forme triangulaire complexe
# Z = A(cos(phi)+i*sin(phi)) quand t=0 avec A = 1
PSK_complex = np.array([np.cos(phi[0]),phi[1]]) + 1j*np.array([np.sin(phi[0]),np.sin(phi[1])])
plt.figure(1)
plt.subplot(3,1,1);plt.grid();plt.text(x=0, y=0.5, s='{}'.format(bin_code,size=50))
plt.plot(t,seq_bin)
plt.subplot(3,1,2);plt.grid();plt.ylim(-3.5,3.5);plt.xlabel('time');plt.ylabel('Amplitude');plt.title('Ask')
plt.plot(t,ASK)
plt.subplot(3,1,3);plt.grid();plt.ylim(-1.5,1.5);plt.xlabel('time');plt.ylabel('Amplitude');plt.title('PSK')
plt.plot(t,PSK)
plt.show()
plt.figure(2)
argand(ASK_complex,'ASK')
argand(PSK_complex,'PSK')
