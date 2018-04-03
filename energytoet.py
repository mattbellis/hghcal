import time
import sys
import matplotlib.pylab as plt
import numpy as np
import ROOT

filenames = sys.argv[1:]

if type(filenames) == str:
    filenames = [filenames]

energies = []
etas = []
thetas = []
layers = []
energiesLAYER = []
mippts = []
Emips = []
mipptsLAYER = []

for i in range(50):
    energiesLAYER.append([])
    mipptsLAYER.append([])

fnum = 0

for filename in filenames:
    energies.append([])
    etas.append([])
    thetas.append([])
    mippts.append([])
    Emips.append([])
    layers.append([])
    
    
    f = ROOT.TFile(filename)
    #f.cd("hgcalTriggerNtuplizer")

    t = f.Get("hgcalTriggerNtuplizer/HGCalTriggerNtuple")
    #t.Print()
    
    nentries = t.GetEntries()
    #for entry in range(nentries):
    for entry in range(3):
   
        t.GetEntry(entry)
        if(int(entry) % 100 == 0):
            print(entry)

        energy = t.tc_energy
        mippt = t.tc_mipPt
        eta = t.tc_eta
        layer = t.tc_layer

        etatmp = np.array(eta)
        mippttmp = np.array(mippt)
        theta = 2 * np.arctan(np.exp(-1*etatmp))
   
        Emipstmp = mippttmp / np.sin(theta) 
    
        energies[fnum] += (energy)
        mippts[fnum] += (mippt)
        Emips[fnum] += (Emipstmp.tolist())
        etas[fnum] += (eta)
        thetas[fnum] += theta.tolist()
        layers[fnum] += (layer)
    
        
    fnum += 1

print("Ran over all the data...")

print(type(etas[0]))
print(len(etas))
   
etas = np.array(etas)[0]
layers = np.array(layers)[0]
energies = np.array(energies)[0]
mippts = np.array(mippts)[0]
Emips = np.array(Emips)[0]

print(type(etas))
print(len(etas))

################################################################################
# Histogram the basic quantities 
################################################################################
plt.figure(figsize=(8,8))
plt.subplot(2,3,1)
plt.hist(etas,bins=100)
plt.xlabel(r"$\eta$",fontsize=18)

plt.subplot(2,3,2)
plt.hist(layers,bins=60,range=(0,30))
plt.xlabel("Layer",fontsize=18)

plt.subplot(2,3,3)
plt.hist(energies,bins=100,range=(0,2))
plt.xlabel("Energy",fontsize=18)

plt.subplot(2,3,4)
plt.hist(mippts,bins=100,range=(0,10))
plt.xlabel("mippt",fontsize=18)

plt.subplot(2,3,5)
plt.hist(Emips,bins=100,range=(0,10))
plt.xlabel("Energy (mip)",fontsize=18)

plt.tight_layout()

################################################################################
# Get a list of masks (selection criteria) based on eta and layer
################################################################################

####### Eta
print('etamasks')
etasmask = []
cut = 1.25
etacuts = []
cutwidth = 0.025
cutstep = 0.25
for i in range(10):
    etacuts.append((cut,cut+cutwidth))
    if i == 0:
        etas1 = abs(etas) < cut
        #etas1 = etas1.astype(np.int)
        etasmask.append(etas1)
    else:
        etas1 = (abs(etas) < cut + cutwidth) & (abs(etas) >= cut)   
        #etas1 = etas1.astype(np.int)
        etasmask.append(etas1)

    cut += cutstep

etasmask = np.array(etasmask)


####### Layer
print('layermask')
layermask = []
for g in range(30):
    #layermask.append([])
    layermaskt = layers ==  g+1
    #layermaskt = layermaskt.astype(np.int)
    layermask.append(layermaskt)

x1 = 0
y1 = 0
x2 = 1
y2 = 10

################################################################################
cut = 1.475
plt.figure(figsize=(9,9))
plt.title('Eta cuts')

for g in range(len(etasmask)):
    plt.subplot(4,4,g+1)
    plt.xlabel('energy(gev)')
    #plt.ylabel('mippt')
    plt.ylabel('energy(mip)')
    plt.xlim(x1,x2)
    plt.ylim(y1,y2)
    #x = energies*etasmask[g]
    #y = mippts*etasmask[g]
    #plt.plot(x[0],y[0],'.',label='Cut: ' + str(cut))
    print(len(energies),len(etasmask[g]),len(etas))
    x = energies[etasmask[g]]
    #y = mippts[etasmask[g]]
    y = Emips[etasmask[g]]
    plt.plot(x,y,'.',markersize=2,alpha=0.3,label=str(etacuts[g][0]) + r'< $\eta$ ' + str(etacuts[g][1]))
    print(g)
    plt.legend()
    #cut += .025

plt.figure(figsize=(10,10))
plt.xlabel('energy(gev)')
#plt.ylabel('mippt')
plt.ylabel('energy(mip)')
cut = 1.475

for i in range(len(etasmask)):
    x = energies[etasmask[i]]
    #y = mippts[etasmask[i]]
    y = Emips[etasmask[i]]
    plt.plot(x,y,'.',markersize=5,alpha=0.3,label=str(etacuts[i][0]) + r'< $\eta$ ' + str(etacuts[i][1]))
    #cut += .025

plt.xlim(x1,x2)
plt.ylim(y1,y2)
plt.legend(markerscale=5)

################################################################################

plt.figure(figsize=(12,8))
#plt.gcf().subplots_adjust(hspace=0.01, wspace=0.01) 
plt.xlabel('energy(gev)')
#plt.ylabel('mippt')
plt.ylabel('energy(mip)')

for i in range(len(layermask)):
    plt.subplot(3,5,int(i/2)+1)
    x = energies[layermask[i]]
    #y = mippts[layermask[i]]
    y = Emips[layermask[i]]
    plt.plot(x,y,'.',markersize=3,label='Layer: ' + str(i+1))

    plt.xlim(x1,x2)
    plt.ylim(y1,y2)
    plt.legend(markerscale=5)
    #plt.gca().set_aspect('equal')


    if i>20:
        plt.xlabel('energy(gev)')
    if i%10==0:
        plt.ylabel('energy(mip)')

plt.tight_layout()
plt.subplots_adjust(wspace=0, hspace=0)



plt.show()
exit()
################################################################################

x1 = 0
y1 = 0
x2 = 4
y2 = 4

plt.figure(figsize=(10,10))
for j in range(len(etasmask)):
    plt.subplot(3,3,j+1)
    for i in range(len(layermask)):
        x = energies*etasmask[j]
        x *= layermask[i]
        y = energies*etasmask[j]
        y *= layermask[i]
        plt.plot(x[0],y[0],'.')
        plt.xlim(x1,x2)
        plt.ylim(y1,y2)


plt.show()
