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
for i in range(nentries):

    t.GetEntry(i)

    print(i)
    x = t.multiclus_energy

    #print(len(x))
    
    layer = t.rechit_layer
    layers.append(layer)





plt.figure()
plt.hist(layers)
plt.show()
