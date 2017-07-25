import numpy as np
import matplotlib.pylab as plt

import ROOT

import sys

infile = sys.argv[1]

f = ROOT.TFile(infile)

t = f.Get("ana/hgc")

#t = f.Get("ana")
#t = t.Get("hgc")

# Definitions here
# https://github.com/CMS-HGCAL/reco-ntuples/blob/master/Definitions.md
t.Print()

# Found some of the definitions here
# CaloCluster
# http://cmsdoxygen.web.cern.ch/cmsdoxygen/CMSSW_9_2_1/doc/html/d4/d06/classreco_1_1CaloCluster.html

nentries = t.GetEntries()
layers = []
wafers = []
cells = []
x = []
y = []
z = []

rece = []

for i in range(nentries):

    t.GetEntry(i)

    print(i)
    #x = t.multiclus_energy
    #print(len(x))
    
    layer = t.rechit_layer
    #layers.append(layer)
    print("layer", layer[0])
    wafer = t.rechit_wafer
    #wafers.append(wafer)
    rx = t.rechit_x
    ry = t.rechit_y
    rz = t.rechit_z

    cell = t.rechit_cell
    #cells.append(cell)
    print(len(cell))
    
    rechit_energy = t.rechit_energy
    print(type(rechit_energy))
    print("renergy", len(rechit_energy))
    print("rlayer", len(layer))
    print("rwafer", len(wafer))
    print("rcell", len(cell))
    #for r,l,w,c,xpt,ypt,zpt in zip(rechit_energy,layer,wafer,cell,rx,ry,rz):
    rece += rechit_energy
    layers += layer
    wafers += wafer
    cells += cell
    x += rx
    y += ry
    z += rz

plt.figure()
plt.hist(rece,bins=100,range=(0,0.6))
plt.xlabel("rechit_energy")
plt.show()
'''
plt.figure()
plt.hist(layers)
plt.xlabel("Layers")

plt.figure()
plt.hist(wafers)
plt.xlabel("Wafers")
