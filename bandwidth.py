import numpy as np
import matplotlib.pylab as plt
import matplotlib.cm as cm

import mpl_scatter_density

import ROOT

import sys


infile = sys.argv[1]

f = ROOT.TFile(infile)

t = f.Get("ana/hgc")

nentries = t.GetEntries()
layers = []
wafers = []
cells = []
x = []
y = []
z = []

t.GetEntry(0)

layer = t.rechit_layer
wafer = t.rechit_wafer
rx = t.rechit_x
ry = t.rechit_y
rz = t.rechit_z
cell = t.rechit_cell
rechit_energy = t.rechit_energy

rece += rechit_energy
layers += layer
wafers += wafer
cells += cell
x += rx
y += ry
z += rz


