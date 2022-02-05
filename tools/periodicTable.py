from chemlib import PeriodicTable
import chemlib
stolendatafromchemlib = ''',AtomicNumber,Element,Symbol,AtomicMass,Neutrons,Protons,Electrons,Period,Group,Phase,Radioactive,Natural,Metal,Nonmetal,Metalloid,Type,AtomicRadius,Electronegativity,FirstIonization,Density,MeltingPoint,BoilingPoint,Isotopes,Discoverer,Year,SpecificHeat,Shells,Valence,Config,MassNumber
0,1.0,Hydrogen,H,1.008,0.0,1.0,1.0,1.0,1.0,gas,False,True,False,True,False,Nonmetal,0.79,2.2,13.5984,0.0000899,14.175,20.28,3.0,Cavendish,1766,14.304,1.0,1.0,1s1,1.0
1,2.0,Helium,He,4.002,2.0,2.0,2.0,1.0,18.0,gas,False,True,False,True,False,Noble Gas,0.49,,24.5874,0.000179,Unknown,4.22,5.0,Janssen,1868,5.193,1.0,0.0,1s2,4.0
2,3.0,Lithium,Li,6.941,4.0,3.0,3.0,2.0,1.0,solid,False,True,True,False,False,Alkali Metal,2.1,0.98,5.3917,0.534,453.85,1615,5.0,Arfvedson,1817,3.582,2.0,1.0,[He] 2s1,7.0
3,4.0,Beryllium,Be,9.012,5.0,4.0,4.0,2.0,2.0,solid,False,True,True,False,False,Alkaline Earth Metal,1.4,1.57,9.3227,1.85,1560.15,2742,6.0,Vaulquelin,1798,1.825,2.0,2.0,[He] 2s2,9.0
4,5.0,Boron,B,10.811,6.0,5.0,5.0,2.0,13.0,solid,False,True,False,False,True,Metalloid,1.2,2.04,8.298,2.34,2573.15,4200,6.0,Gay-Lussac,1808,1.026,2.0,3.0,[He] 2s2 2p1,11.0
5,6.0,Carbon,C,12.011,6.0,6.0,6.0,2.0,14.0,solid,False,True,False,True,False,Nonmetal,0.91,2.55,11.2603,2.27,3948.15,4300,7.0,Prehistoric,Unknown,0.709,2.0,4.0,[He] 2s2 2p2,12.0
6,7.0,Nitrogen,N,14.007,7.0,7.0,7.0,2.0,15.0,gas,False,True,False,True,False,Nonmetal,0.75,3.04,14.5341,0.00125,63.29,77.36,8.0,Rutherford,1772,1.04,2.0,5.0,[He] 2s2 2p3,14.0
7,8.0,Oxygen,O,15.999,8.0,8.0,8.0,2.0,16.0,gas,False,True,False,True,False,Nonmetal,0.65,3.44,13.6181,0.00143,50.5,90.2,8.0,Priestley/Scheele,1774,0.917999999999999,2.0,6.0,[He] 2s2 2p4,16.0
8,9.0,Fluorine,F,18.998,10.0,9.0,9.0,2.0,17.0,gas,False,True,False,True,False,Halogen,0.57,3.98,17.4228,0.0017,53.63,85.03,6.0,Moissan,1886,0.824,2.0,7.0,[He] 2s2 2p5,19.0
9,10.0,Neon,Ne,20.18,10.0,10.0,10.0,2.0,18.0,gas,False,True,False,True,False,Noble Gas,0.51,,21.5645,0.0009,24.703,27.07,8.0,Ramsay and Travers,1898,1.03,2.0,8.0,[He] 2s2 2p6,20.0
10,11.0,Sodium,Na,22.99,12.0,11.0,11.0,3.0,1.0,solid,False,True,True,False,False,Alkali Metal,2.2,0.93,5.1391,0.971,371.15,1156,7.0,Davy,1807,1.228,3.0,1.0,[Ne] 3s1,23.0
11,12.0,Magnesium,Mg,24.305,12.0,12.0,12.0,3.0,2.0,solid,False,True,True,False,False,Alkaline Earth Metal,1.7,1.31,7.6462,1.74,923.15,1363,8.0,Black,1755,1.023,3.0,2.0,[Ne] 3s2,24.0
12,13.0,Aluminum,Al,26.982,14.0,13.0,13.0,3.0,13.0,solid,False,True,True,False,False,Metal,1.8,1.61,5.9858,2.7,933.4,2792,8.0,Wshler,1827,0.897,3.0,3.0,[Ne] 3s2 3p1,27.0
13,14.0,Silicon,Si,28.086,14.0,14.0,14.0,3.0,14.0,solid,False,True,False,False,True,Metalloid,1.5,1.9,8.1517,2.33,1683.15,3538,8.0,Berzelius,1824,0.705,3.0,4.0,[Ne] 3s2 3p2,28.0
14,15.0,Phosphorus,P,30.974,16.0,15.0,15.0,3.0,15.0,solid,False,True,False,True,False,Nonmetal,1.2,2.19,10.4867,1.82,317.25,553,7.0,BranBrand,1669,0.769,3.0,5.0,[Ne] 3s2 3p3,31.0
15,16.0,Sulfur,S,32.065,16.0,16.0,16.0,3.0,16.0,solid,False,True,False,True,False,Nonmetal,1.1,2.58,10.36,2.07,388.51,717.8,10.0,Prehistoric,Unknown,0.71,3.0,6.0,[Ne] 3s2 3p4,32.0
16,17.0,Chlorine,Cl,35.453,18.0,17.0,17.0,3.0,17.0,gas,False,True,False,True,False,Halogen,0.97,3.16,12.9676,0.00321,172.31,239.11,11.0,Scheele,1774,0.479,3.0,7.0,[Ne] 3s2 3p5,35.0
17,18.0,Argon,Ar,39.948,22.0,18.0,18.0,3.0,18.0,gas,False,True,False,True,False,Noble Gas,0.88,,15.7596,0.00178,83.96,87.3,8.0,Rayleigh and Ramsay,1894,0.52,3.0,8.0,[Ne] 3s2 3p6,40.0
18,19.0,Potassium,K,39.098,20.0,19.0,19.0,4.0,1.0,solid,False,True,True,False,False,Alkali Metal,2.8,0.82,4.3407,0.862,336.5,1032,10.0,Davy,1807,0.757,4.0,1.0,[Ar] 4s1,39.0
19,20.0,Calcium,Ca,40.078,20.0,20.0,20.0,4.0,2.0,solid,False,True,True,False,False,Alkaline Earth Metal,2.2,1.0,6.1132,1.54,1112.15,1757,14.0,Davy,1808,0.647,4.0,2.0,[Ar] 4s2,40.0
20,21.0,Scandium,Sc,44.956,24.0,21.0,21.0,4.0,3.0,solid,False,True,True,False,False,Transition Metal,2.1,1.36,6.5615,2.99,1812.15,3109,15.0,Nilson,1878,0.568,4.0,0.0,[Ar] 3d1 4s2,45.0
21,22.0,Titanium,Ti,47.867,26.0,22.0,22.0,4.0,4.0,solid,False,True,True,False,False,Transition Metal,2,1.54,6.8281,4.54,1933.15,3560,9.0,Gregor,1791,0.523,4.0,0.0,[Ar] 3d2 4s2,48.0
22,23.0,Vanadium,V,50.942,28.0,23.0,23.0,4.0,5.0,solid,False,True,True,False,False,Transition Metal,1.9,1.63,6.7462,6.11,2175.15,3680,9.0,   del Rio,1801,0.489,4.0,0.0,[Ar] 3d3 4s2,51.0
23,24.0,Chromium,Cr,51.996,28.0,24.0,24.0,4.0,6.0,solid,False,True,True,False,False,Transition Metal,1.9,1.66,6.7665,7.15,2130.15,2944,9.0,Vauquelin,1797,0.449,4.0,0.0,[Ar] 3d5 4s1,52.0
24,25.0,Manganese,Mn,54.938,30.0,25.0,25.0,4.0,7.0,solid,False,True,True,False,False,Transition Metal,1.8,1.55,7.434,7.44,1519.15,2334,11.0,"Gahn, Scheele",1774,0.479,4.0,0.0,[Ar] 3d5 4s2,55.0
25,26.0,Iron,Fe,55.845,30.0,26.0,26.0,4.0,8.0,solid,False,True,True,False,False,Transition Metal,1.7,1.83,7.9024,7.87,1808.15,3134,10.0,Prehistoric,Unknown,0.449,4.0,0.0,[Ar] 3d6 4s2,56.0
26,27.0,Cobalt,Co,58.933,32.0,27.0,27.0,4.0,9.0,solid,False,True,True,False,False,Transition Metal,1.7,1.88,7.881,8.86,1768.15,3200,14.0,Brandt,1735,0.421,4.0,0.0,[Ar] 3d7 4s2,59.0
27,28.0,Nickel,Ni,58.69300000000001,31.0,28.0,28.0,4.0,10.0,solid,False,True,True,False,False,Transition Metal,1.6,1.91,7.6398,8.91,1726.15,3186,11.0,Cronstedt,1751,0.444,4.0,0.0,[Ar] 3d8 4s2,59.0
28,29.0,Copper,Cu,63.54600000000001,35.0,29.0,29.0,4.0,11.0,solid,False,True,True,False,False,Transition Metal,1.6,1.9,7.7264,8.96,1357.75,2835,11.0,Prehistoric,Unknown,0.385,4.0,0.0,[Ar] 3d10 4s1,64.0
29,30.0,Zinc,Zn,65.38,35.0,30.0,30.0,4.0,12.0,solid,False,True,True,False,False,Transition Metal,1.5,1.65,9.3942,7.13,692.88,1180,15.0,Prehistoric,Unknown,0.387999999999999,4.0,0.0,[Ar] 3d10 4s2,65.0
30,31.0,Gallium,Ga,69.723,39.0,31.0,31.0,4.0,13.0,solid,False,True,True,False,False,Metal,1.8,1.81,5.9993,5.91,302.91,2477,14.0,de Boisbaudran,1875,0.371,4.0,3.0,[Ar] 3d10 4s2 4p1,70.0
31,32.0,Germanium,Ge,72.64,41.0,32.0,32.0,4.0,14.0,solid,False,True,False,False,True,Metalloid,1.5,2.01,7.8994,5.32,1211.45,3106,17.0,Winkler,1886,0.32,4.0,4.0,[Ar] 3d10 4s2 4p2,73.0
32,33.0,Arsenic,As,74.922,42.0,33.0,33.0,4.0,15.0,solid,False,True,False,False,True,Metalloid,1.3,2.18,9.7886,5.78,1090.15,887,14.0,Albertus Magnus,1250,0.328999999999999,4.0,5.0,[Ar] 3d10 4s2 4p3,75.0
33,34.0,Selenium,Se,78.96,45.0,34.0,34.0,4.0,16.0,solid,False,True,False,True,False,Nonmetal,1.2,2.55,9.7524,4.81,494.15,958,20.0,Berzelius,1817,0.321,4.0,6.0,[Ar] 3d10 4s2 4p4,79.0
34,35.0,Bromine,Br,79.904,45.0,35.0,35.0,4.0,17.0,liq,False,True,False,True,False,Halogen,1.1,2.96,11.8138,3.12,266.05,332,19.0,Balard,1826,0.474,4.0,7.0,[Ar] 3d10 4s2 4p5,80.0
35,36.0,Krypton,Kr,83.7979999999999,48.0,36.0,36.0,4.0,18.0,gas,False,True,False,True,False,Noble Gas,1,,13.9996,0.00373,115.93,119.93,23.0,Ramsay and Travers,1898,0.248,4.0,8.0,[Ar] 3d10 4s2 4p6,84.0
36,37.0,Rubidium,Rb,85.4679999999999,48.0,37.0,37.0,5.0,1.0,solid,False,True,True,False,False,Alkali Metal,3,0.82,4.1771,1.53,312.79,961,20.0,Bunsen and Kirchoff,1861,0.363,5.0,1.0,[Kr] 5s1,85.0
37,38.0,Strontium,Sr,87.62,50.0,38.0,38.0,5.0,2.0,solid,False,True,True,False,False,Alkaline Earth Metal,2.5,0.95,5.6949,2.64,1042.15,1655,18.0,Davy,1808,0.301,5.0,2.0,[Kr] 5s2,88.0
38,39.0,Yttrium,Y,88.906,50.0,39.0,39.0,5.0,3.0,solid,False,True,True,False,False,Transition Metal,2.3,1.22,6.2173,4.47,1799.15,3609,21.0,Gadolin,1794,0.298,5.0,0.0,[Kr] 4d1 5s2,89.0
39,40.0,Zirconium,Zr,91.2239999999999,51.0,40.0,40.0,5.0,4.0,solid,False,True,True,False,False,Transition Metal,2.2,1.33,6.6339,6.51,2125.15,4682,20.0,Klaproth,1789,0.278,5.0,0.0,[Kr] 4d2 5s2,91.0
40,41.0,Niobium,Nb,92.906,52.0,41.0,41.0,5.0,5.0,solid,False,True,True,False,False,Transition Metal,2.1,1.6,6.7589,8.57,2741.15,5017,24.0,Hatchett,1801,0.265,5.0,0.0,[Kr] 4d4 5s1,93.0
41,42.0,Molybdenum,Mo,95.96,54.0,42.0,42.0,5.0,6.0,solid,False,True,True,False,False,Transition Metal,2,2.16,7.0924,10.2,2890.15,4912,20.0,Scheele,1778,0.251,5.0,0.0,[Kr] 4d5 5s1,96.0
42,43.0,Technetium,Tc,98.0,55.0,43.0,43.0,5.0,7.0,artificial,True,False,True,False,False,Transition Metal,2,1.9,7.28,11.5,2473.15,5150,23.0,Perrier and Segr�,1937,Unknown,5.0,0.0,[Kr] 4d5 5s2,98.0
43,44.0,Ruthenium,Ru,101.07,57.0,44.0,44.0,5.0,8.0,solid,False,True,True,False,False,Transition Metal,1.9,2.2,7.3605,12.4,2523.15,4423,16.0,Klaus,1844,0.238,5.0,0.0,[Kr] 4d7 5s1,101.0
44,45.0,Rhodium,Rh,102.906,58.0,45.0,45.0,5.0,9.0,solid,False,True,True,False,False,Transition Metal,1.8,2.28,7.4589,12.4,2239.15,3968,20.0,Wollaston,1803,0.243,5.0,0.0,[Kr] 4d8 5s1,103.0
45,46.0,Palladium,Pd,106.42,60.0,46.0,46.0,5.0,10.0,solid,False,True,True,False,False,Transition Metal,1.8,2.2,8.3369,12,1825.15,3236,21.0,Wollaston,1803,0.244,5.0,0.0,[Kr] 4d10,106.0
46,47.0,Silver,Ag,107.868,61.0,47.0,47.0,5.0,11.0,solid,False,True,True,False,False,Transition Metal,1.8,1.93,7.5762,10.5,1234.15,2435,27.0,Prehistoric,Unknown,0.235,5.0,0.0,[Kr] 4d10 5s1,108.0
47,48.0,Cadmium,Cd,112.411,64.0,48.0,48.0,5.0,12.0,solid,False,True,True,False,False,Transition Metal,1.7,1.69,8.9938,8.69,594.33,1040,22.0,Stromeyer,1817,0.231999999999999,5.0,0.0,[Kr] 4d10 5s2,112.0
48,49.0,Indium,In,114.818,66.0,49.0,49.0,5.0,13.0,solid,False,True,True,False,False,Metal,2,1.78,5.7864,7.31,429.91,2345,34.0,Reich and Richter,1863,0.233,5.0,3.0,[Kr] 4d10 5s2 5p1,115.0
49,50.0,Tin,Sn,118.71,69.0,50.0,50.0,5.0,14.0,solid,False,True,True,False,False,Metal,1.7,1.96,7.3439,7.29,505.21,2875,28.0,Prehistoric,Unknown,0.228,5.0,4.0,[Kr] 4d10 5s2 5p2,119.0
50,51.0,Antimony,Sb,121.76,71.0,51.0,51.0,5.0,15.0,solid,False,True,False,False,True,Metalloid,1.5,2.05,8.6084,6.69,904.05,1860,29.0,Early historic times,Unknown,0.207,5.0,5.0,[Kr] 4d10 5s2 5p3,122.0
51,52.0,Tellurium,Te,127.6,76.0,52.0,52.0,5.0,16.0,solid,False,True,False,False,True,Metalloid,1.4,2.1,9.0096,6.23,722.8,1261,29.0,von Reichenstein,1782,0.201999999999999,5.0,6.0,[Kr] 4d10 5s2 5p4,128.0
52,53.0,Iodine,I,126.904,74.0,53.0,53.0,5.0,17.0,solid,False,True,False,True,False,Halogen,1.3,2.66,10.4513,4.93,386.65,457.4,24.0,Courtois,1811,0.214,5.0,7.0,[Kr] 4d10 5s2 5p5,127.0
53,54.0,Xenon,Xe,131.293,77.0,54.0,54.0,5.0,18.0,gas,False,True,False,True,False,Noble Gas,1.2,,12.1298,0.00589,161.45,165.03,31.0,Ramsay and Travers,1898,0.158,5.0,8.0,[Kr] 4d10 5s2 5p6,131.0
54,55.0,Cesium,Cs,132.905,78.0,55.0,55.0,6.0,1.0,solid,False,True,True,False,False,Alkali Metal,3.3,0.79,3.8939,1.87,301.7,944,22.0,Bunsen and Kirchoff,1860,0.242,6.0,1.0,[Xe] 6s1,133.0
55,56.0,Barium,Ba,137.327,81.0,56.0,56.0,6.0,2.0,solid,False,True,True,False,False,Alkaline Earth Metal,2.8,0.89,5.2117,3.59,1002.15,2170,25.0,Davy,1808,0.204,6.0,2.0,[Xe] 6s2,137.0
56,57.0,Lanthanum,La,138.905,82.0,57.0,57.0,6.0,3.0,solid,False,True,True,False,False,Lanthanide,2.7,1.1,5.5769,6.15,1193.15,3737,19.0,Mosander,1839,0.195,6.0,0.0,[Xe] 5d1 6s2,139.0
57,58.0,Cerium,Ce,140.116,82.0,58.0,58.0,6.0,3.0,solid,False,True,True,False,False,Lanthanide,2.7,1.12,5.5387,6.77,1071.15,3716,19.0,Berzelius,1803,0.192,6.0,0.0,[Xe] 4f1 5d1 6s2,140.0
58,59.0,Praseodymium,Pr,140.908,82.0,59.0,59.0,6.0,3.0,solid,False,True,True,False,False,Lanthanide,2.7,1.13,5.473,6.77,1204.15,3793,15.0,von Welsbach,1885,0.193,6.0,0.0,[Xe] 4f3 6s2,141.0
59,60.0,Neodymium,Nd,144.24200000000005,84.0,60.0,60.0,6.0,3.0,solid,False,True,True,False,False,Lanthanide,2.6,1.14,5.525,7.01,1289.15,3347,16.0,von Welsbach,1885,0.19,6.0,0.0,[Xe] 4f4 6s2,144.0
60,61.0,Promethium,Pm,145.0,84.0,61.0,61.0,6.0,3.0,artificial,True,False,True,False,False,Lanthanide,2.6,1.13,5.582,7.26,1204.15,3273,14.0,Marinsky et al.,1945,Unknown,6.0,0.0,[Xe] 4f5 6s2,145.0
61,62.0,Samarium,Sm,150.36,88.0,62.0,62.0,6.0,3.0,solid,False,True,True,False,False,Lanthanide,2.6,1.17,5.6437,7.52,1345.15,2067,17.0,Boisbaudran,1879,0.196999999999999,6.0,0.0,[Xe] 4f6 6s2,150.0
62,63.0,Europium,Eu,151.964,89.0,63.0,63.0,6.0,3.0,solid,False,True,True,False,False,Lanthanide,2.6,1.2,5.6704,5.24,1095.15,1802,21.0,Demarcay,1901,0.182,6.0,0.0,[Xe] 4f7 6s2,152.0
63,64.0,Gadolinium,Gd,157.25,93.0,64.0,64.0,6.0,3.0,solid,False,True,True,False,False,Lanthanide,2.5,1.2,6.1501,7.9,1585.15,3546,17.0,de Marignac,1880,0.236,6.0,0.0,[Xe] 4f7 5d1 6s2,157.0
64,65.0,Terbium,Tb,158.925,94.0,65.0,65.0,6.0,3.0,solid,False,True,True,False,False,Lanthanide,2.5,1.2,5.8638,8.23,1630.15,3503,24.0,Mosander,1843,0.182,6.0,0.0,[Xe] 4f9 6s2,159.0
65,66.0,Dysprosium,Dy,162.5,97.0,66.0,66.0,6.0,3.0,solid,False,True,True,False,False,Lanthanide,2.5,1.22,5.9389,8.55,1680.15,2840,21.0,de Boisbaudran,1886,0.17,6.0,0.0,[Xe] 4f10 6s2,163.0
66,67.0,Holmium,Ho,164.93,98.0,67.0,67.0,6.0,3.0,solid,False,True,True,False,False,Lanthanide,2.5,1.23,6.0215,8.8,1743.15,2993,29.0,Delafontaine and Soret,1878,0.165,6.0,0.0,[Xe] 4f11 6s2,165.0
67,68.0,Erbium,Er,167.25900000000001,99.0,68.0,68.0,6.0,3.0,solid,False,True,True,False,False,Lanthanide,2.5,1.24,6.1077,9.07,1795.15,3503,16.0,Mosander,1843,0.168,6.0,0.0,[Xe] 4f12 6s2,167.0
68,69.0,Thulium,Tm,168.93400000000003,100.0,69.0,69.0,6.0,3.0,solid,False,True,True,False,False,Lanthanide,2.4,1.25,6.1843,9.32,1818.15,2223,18.0,Cleve,1879,0.16,6.0,0.0,[Xe] 4f13 6s2,169.0
69,70.0,Ytterbium,Yb,173.054,103.0,70.0,70.0,6.0,3.0,solid,False,True,True,False,False,Lanthanide,2.4,1.1,6.2542,6.97,1097.15,1469,16.0,Marignac,1878,0.155,6.0,0.0,[Xe] 4f14 6s2,173.0
70,71.0,Lutetium,Lu,174.967,104.0,71.0,71.0,6.0,3.0,solid,False,True,True,False,False,Lanthanide,2.3,1.27,5.4259,9.84,1936.15,3675,22.0,Urbain/ von Welsbach,1907,0.154,6.0,0.0,[Xe] 4f14 5d1 6s2,175.0
71,72.0,Hafnium,Hf,178.49,106.0,72.0,72.0,6.0,4.0,solid,False,True,True,False,False,Transition Metal,2.2,1.3,6.8251,13.3,2500.15,4876,17.0,Coster and von Hevesy,1923,0.144,6.0,0.0,[Xe] 4f14 5d2 6s2,178.0
72,73.0,Tantalum,Ta,180.947999999999,108.0,73.0,73.0,6.0,5.0,solid,False,True,True,False,False,Transition Metal,2.1,1.5,7.5496,16.7,3269.15,5731,19.0,Ekeberg,1801,0.14,6.0,0.0,[Xe] 4f14 5d3 6s2,181.0
73,74.0,Wolfram,W,183.84,110.0,74.0,74.0,6.0,6.0,solid,False,True,True,False,False,Transition Metal,2,2.36,7.864,19.3,3680.15,5828,22.0,J. and F. d'Elhuyar,1783,0.132,6.0,0.0,[Xe] 4f14 5d4 6s2,184.0
74,75.0,Rhenium,Re,186.207,111.0,75.0,75.0,6.0,7.0,solid,False,True,True,False,False,Transition Metal,2,1.9,7.8335,21,3453.15,5869,21.0,"Noddack, Berg, and Tacke",1925,0.136999999999999,6.0,0.0,[Xe] 4f14 5d5 6s2,186.0
75,76.0,Osmium,Os,190.23,114.0,76.0,76.0,6.0,8.0,solid,False,True,True,False,False,Transition Metal,1.9,2.2,8.4382,22.6,3300.15,5285,19.0,Tennant,1803,0.13,6.0,0.0,[Xe] 4f14 5d6 6s2,190.0
76,77.0,Iridium,Ir,192.217,115.0,77.0,77.0,6.0,9.0,solid,False,True,True,False,False,Transition Metal,1.9,2.2,8.967,22.6,2716.15,4701,25.0,Tennant,1804,0.131,6.0,0.0,[Xe] 4f14 5d7 6s2,192.0
77,78.0,Platinum,Pt,195.084,117.0,78.0,78.0,6.0,10.0,solid,False,True,True,False,False,Transition Metal,1.8,2.28,8.9587,21.5,2045.15,4098,32.0,Ulloa/Wood,1735,0.133,6.0,0.0,[Xe] 4f14 5d9 6s1,195.0
78,79.0,Gold,Au,196.967,118.0,79.0,79.0,6.0,11.0,solid,False,True,True,False,False,Transition Metal,1.8,2.54,9.2255,19.3,1337.73,3129,21.0,Prehistoric,Unknown,0.129,6.0,0.0,[Xe] 4f14 5d10 6s1,197.0
79,80.0,Mercury,Hg,200.59,121.0,80.0,80.0,6.0,12.0,liq,False,True,True,False,False,Transition Metal,1.8,2.0,10.4375,13.5,234.43,630,26.0,Prehistoric,Unknown,0.14,6.0,0.0,[Xe] 4f14 5d10 6s2,201.0
80,81.0,Thallium,Tl,204.38299999999904,123.0,81.0,81.0,6.0,13.0,solid,False,True,True,False,False,Metal,2.1,2.04,6.1082,11.9,577.15,1746,28.0,Crookes,1861,0.129,6.0,3.0,[Xe] 4f14 5d10 6s2 6p1,204.0
81,82.0,Lead,Pb,207.2,125.0,82.0,82.0,6.0,14.0,solid,False,True,True,False,False,Metal,1.8,2.33,7.4167,11.3,600.75,2022,29.0,Prehistoric,Unknown,0.129,6.0,4.0,[Xe] 4f14 5d10 6s2 6p2,207.0
82,83.0,Bismuth,Bi,208.98,126.0,83.0,83.0,6.0,15.0,solid,False,True,True,False,False,Metal,1.6,2.02,7.2856,9.81,544.67,1837,19.0,Geoffroy the Younger,1753,0.122,6.0,5.0,[Xe] 4f14 5d10 6s2 6p3,209.0
83,84.0,Polonium,Po,210.0,126.0,84.0,84.0,6.0,16.0,solid,True,True,False,False,True,Metal,1.5,2.0,8.417,9.32,527.15,1235,34.0,Curie,1898,Unknown,6.0,6.0,[Xe] 4f14 5d10 6s2 6p4,210.0
84,85.0,Astatine,At,210.0,125.0,85.0,85.0,6.0,17.0,solid,True,True,False,True,False,Metalloid,1.4,2.2,9.3,7,575.15,610,21.0,Corson et al.,1940,Unknown,6.0,7.0,[Xe] 4f14 5d10 6s2 6p5,210.0
85,86.0,Radon,Rn,222.0,136.0,86.0,86.0,6.0,18.0,gas,True,True,True,False,False,Noble Gas,1.3,,10.7485,0.00972999999999999,202.15,211.3,20.0,Dorn,1900,0.094,6.0,8.0,[Xe] 4f14 5d10 6s2 6p6,222.0
86,87.0,Francium,Fr,223.0,136.0,87.0,87.0,7.0,1.0,solid,True,True,True,False,False,Alkali Metal,Unknown,0.7,4.0727,1.87,300.15,950,21.0,Perey,1939,Unknown,7.0,1.0,[Rn] 7s1,223.0
87,88.0,Radium,Ra,226.0,138.0,88.0,88.0,7.0,2.0,solid,True,True,True,False,False,Alkaline Earth Metal,Unknown,0.9,5.2784,5.5,973.15,2010,15.0,Pierre and Marie Curie,1898,Unknown,7.0,2.0,[Rn] 7s2,226.0
88,89.0,Actinium,Ac,227.0,138.0,89.0,89.0,7.0,3.0,solid,True,True,True,False,False,Actinide,Unknown,1.1,5.17,10.1,1323.15,3471,11.0,Debierne/Giesel,1899,0.12,7.0,0.0,[Rn] 6d1 7s2,227.0
89,90.0,Thorium,Th,232.03799999999904,142.0,90.0,90.0,7.0,3.0,solid,True,True,True,False,False,Actinide,Unknown,1.3,6.3067,11.7,2028.15,5061,12.0,Berzelius,1828,0.113,7.0,0.0,[Rn] 6d2 7s2,232.0
90,91.0,Protactinium,Pa,231.035999999999,140.0,91.0,91.0,7.0,3.0,solid,True,True,True,False,False,Actinide,Unknown,1.5,5.89,15.4,1873.15,4300,14.0,Hahn and Meitner,1917,Unknown,7.0,0.0,[Rn] 5f2 6d1 7s2,231.0
91,92.0,Uranium,U,238.02900000000002,146.0,92.0,92.0,7.0,3.0,solid,True,True,True,False,False,Actinide,Unknown,1.38,6.1941,19,1405.15,4404,15.0,Peligot,1841,0.115999999999999,7.0,0.0,[Rn] 5f3 6d1 7s2,238.0
92,93.0,Neptunium,Np,237.0,144.0,93.0,93.0,7.0,3.0,artificial,True,False,True,False,False,Actinide,Unknown,1.36,6.2657,20.5,913.15,4273,153.0,McMillan and Abelson,1940,Unknown,7.0,0.0,[Rn] 5f4 6d1 7s2,237.0
93,94.0,Plutonium,Pu,244.0,150.0,94.0,94.0,7.0,3.0,artificial,True,False,True,False,False,Actinide,Unknown,1.28,6.0262,19.8,913.15,3501,163.0,Seaborg et al.,1940,Unknown,7.0,0.0,[Rn] 5f6 7s2,244.0
94,95.0,Americium,Am,243.0,148.0,95.0,95.0,7.0,3.0,artificial,True,False,True,False,False,Actinide,Unknown,1.3,5.9738,13.7,1267.15,2880,133.0,Seaborg et al.,1944,Unknown,7.0,0.0,[Rn] 5f7 7s2,243.0
95,96.0,Curium,Cm,247.0,151.0,96.0,96.0,7.0,3.0,artificial,True,False,True,False,False,Actinide,Unknown,1.3,5.9915,13.5,1340.15,3383,133.0,Seaborg et al.,1944,Unknown,7.0,0.0,[Rn] 5f7 6d1 7s2,247.0
96,97.0,Berkelium,Bk,247.0,150.0,97.0,97.0,7.0,3.0,artificial,True,False,True,False,False,Actinide,Unknown,1.3,6.1979,14.8,1259.15,983,83.0,Seaborg et al.,1949,Unknown,7.0,0.0,[Rn] 5f9 7s2,247.0
97,98.0,Californium,Cf,251.0,153.0,98.0,98.0,7.0,3.0,artificial,True,False,True,False,False,Actinide,Unknown,1.3,6.2817,15.1,1925.15,1173,123.0,Seaborg et al.,1950,Unknown,7.0,0.0,[Rn] 5f10 7s2,251.0
98,99.0,Einsteinium,Es,252.0,153.0,99.0,99.0,7.0,3.0,artificial,True,False,True,False,False,Actinide,Unknown,1.3,6.42,13.5,1133.15,Unknown,123.0,Ghiorso et al.,1952,Unknown,7.0,0.0,[Rn] 5f11 7s2,252.0
99,100.0,Fermium,Fm,257.0,157.0,100.0,100.0,7.0,3.0,artificial,True,False,True,False,False,Actinide,Unknown,1.3,6.5,Unknown,Unknown,Unknown,103.0,Ghiorso et al.,1953,Unknown,7.0,0.0,[Rn] 5f12 7s2,257.0
100,101.0,Mendelevium,Md,258.0,157.0,101.0,101.0,7.0,3.0,artificial,True,False,True,False,False,Actinide,Unknown,1.3,6.58,Unknown,Unknown,Unknown,33.0,Ghiorso et al.,1955,Unknown,7.0,0.0,[Rn] 5f13 7s2,258.0
101,102.0,Nobelium,No,259.0,157.0,102.0,102.0,7.0,3.0,artificial,True,False,True,False,False,Actinide,Unknown,1.3,6.65,Unknown,Unknown,Unknown,73.0,Ghiorso et al.,1958,Unknown,7.0,0.0,[Rn] 5f14 7s2,259.0
102,103.0,Lawrencium,Lr,262.0,159.0,103.0,103.0,7.0,3.0,artificial,True,False,True,False,False,Actinide,Unknown,,Unknown,Unknown,Unknown,Unknown,203.0,Ghiorso et al.,1961,Unknown,7.0,0.0,[Rn] 5f14 7s2 7p1,262.0
103,104.0,Rutherfordium,Rf,261.0,157.0,104.0,104.0,7.0,4.0,artificial,True,False,True,False,False,Transactinide,Unknown,,Unknown,18.1,Unknown,Unknown,,Ghiorso et al.,1969,Unknown,7.0,0.0,[Rn] 5f14 6d2 7s2,261.0
104,105.0,Dubnium,Db,262.0,157.0,105.0,105.0,7.0,5.0,artificial,True,False,True,False,False,Transactinide,Unknown,,Unknown,39,Unknown,Unknown,,Ghiorso et al.,1970,Unknown,7.0,0.0,[Rn] 5f14 6d3 7s2,262.0
105,106.0,Seaborgium,Sg,266.0,160.0,106.0,106.0,7.0,6.0,artificial,True,False,True,False,False,Transactinide,Unknown,,Unknown,35,Unknown,Unknown,,Ghiorso et al.,1974,Unknown,7.0,0.0,[Rn] 5f14 6d4 7s2,266.0
106,107.0,Bohrium,Bh,264.0,157.0,107.0,107.0,7.0,7.0,artificial,True,False,True,False,False,Transactinide,Unknown,,Unknown,37,Unknown,Unknown,,Armbruster and M�nzenberg,1981,Unknown,7.0,0.0,[Rn] 5f14 6d5 7s2,264.0
107,108.0,Hassium,Hs,267.0,159.0,108.0,108.0,7.0,8.0,artificial,True,False,True,False,False,Transactinide,Unknown,,Unknown,41,Unknown,Unknown,,Armbruster and M�nzenberg,1983,Unknown,7.0,0.0,[Rn] 5f14 6d6 7s2,267.0
108,109.0,Meitnerium,Mt,268.0,159.0,109.0,109.0,7.0,9.0,artificial,True,False,True,False,False,Transactinide,Unknown,,Unknown,35,Unknown,Unknown,,"GSI, Darmstadt, West Germany",1982,Unknown,7.0,0.0,[Rn] 5f14 6d7 7s2,268.0
109,110.0,Darmstadtium ,Ds ,271.0,161.0,110.0,110.0,7.0,10.0,artificial,True,False,True,False,False,Transactinide,Unknown,,Unknown,Unknown,Unknown,Unknown,,Unknown,1994,Unknown,7.0,0.0,[Rn] 5f14 6d9 7s1,271.0
110,111.0,Roentgenium ,Rg ,272.0,161.0,111.0,111.0,7.0,11.0,artificial,True,False,True,False,False,Transactinide,Unknown,,Unknown,Unknown,Unknown,Unknown,,Unknown,1994,Unknown,7.0,0.0,[Rn] 5f14 6d10 7s1,272.0
111,112.0,Copernicium ,Cn ,285.0,173.0,112.0,112.0,7.0,12.0,artificial,True,False,True,False,False,Transactinide,Unknown,,Unknown,Unknown,Unknown,Unknown,,Unknown,1996,Unknown,7.0,0.0,[Rn] 5f14 6d10 7s2,285.0
112,113.0,Nihonium,Nh,284.0,171.0,113.0,113.0,7.0,13.0,artificial,True,False,True,False,False,Transactinide,Unknown,,Unknown,Unknown,Unknown,Unknown,,Unknown,2004,Unknown,7.0,3.0,[Rn] 5f14 6d10 7s2 7p1,284.0
113,114.0,Flerovium,Fl,289.0,175.0,114.0,114.0,7.0,14.0,artificial,True,False,True,False,False,Transactinide,Unknown,,Unknown,Unknown,Unknown,Unknown,,Unknown,1999,Unknown,7.0,4.0,[Rn] 5f14 6d10 7s2 7p2,289.0
114,115.0,Moscovium,Mc,288.0,173.0,115.0,115.0,7.0,15.0,artificial,True,False,True,False,False,Transactinide,Unknown,,Unknown,Unknown,Unknown,Unknown,,Unknown,2010,Unknown,7.0,5.0,[Rn] 5f14 6d10 7s2 7p3,288.0
115,116.0,Livermorium,Lv,292.0,176.0,116.0,116.0,7.0,16.0,artificial,True,False,True,False,False,Transactinide,Unknown,,Unknown,Unknown,Unknown,Unknown,,Unknown,2000,Unknown,7.0,6.0,[Rn] 5f14 6d10 7s2 7p4,292.0
116,117.0,Tennessine,Ts,295.0,178.0,117.0,117.0,7.0,17.0,artificial,True,False,False,True,False,Transactinide,Unknown,,Unknown,Unknown,Unknown,Unknown,,Unknown,2010,Unknown,7.0,7.0,[Rn] 5f14 6d10 7s2 7p5,295.0
117,118.0,Oganesson,Og,294.0,176.0,118.0,118.0,7.0,18.0,artificial,True,False,False,True,False,Noble Gas,Unknown,,Unknown,Unknown,Unknown,Unknown,,Unknown,2006,Unknown,7.0,8.0,[Rn] 5f14 6d10 7s2 7p6,294.0'''

saved={
    'AtomicNumber': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0, 110.0, 111.0, 112.0, 113.0, 114.0, 115.0, 116.0, 117.0, 118.0], 
    'Element': ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Wolfram', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium ', 'Roentgenium ', 'Copernicium ', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson'], 
    'Symbol': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds ', 'Rg ', 'Cn ', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'], 
    'AtomicMass': [1.008, 4.002, 6.941, 9.012, 10.811, 12.011, 14.007, 15.999, 18.998, 20.18, 22.99, 24.305, 26.982, 28.086, 30.974, 32.065, 35.453, 39.948, 39.098, 40.078, 44.956, 47.867, 50.942, 51.996, 54.938, 55.845, 58.933, 58.69300000000001, 63.54600000000001, 65.38, 69.723, 72.64, 74.922, 78.96, 79.904, 83.7979999999999, 85.4679999999999, 87.62, 88.906, 91.2239999999999, 92.906, 95.96, 98.0, 101.07, 102.906, 106.42, 107.868, 112.411, 114.818, 118.71, 121.76, 127.6, 126.904, 131.293, 132.905, 137.327, 138.905, 140.116, 140.908, 144.24200000000005, 145.0, 150.36, 151.964, 157.25, 158.925, 162.5, 164.93, 167.25900000000001, 168.93400000000003, 173.054, 174.967, 178.49, 180.947999999999, 183.84, 186.207, 190.23, 192.217, 195.084, 196.967, 200.59, 204.38299999999904, 207.2, 208.98, 210.0, 210.0, 222.0, 223.0, 226.0, 227.0, 232.03799999999904, 231.035999999999, 238.02900000000002, 237.0, 244.0, 243.0, 247.0, 247.0, 251.0, 252.0, 257.0, 258.0, 259.0, 262.0, 261.0, 262.0, 266.0, 264.0, 267.0, 268.0, 271.0, 272.0, 285.0, 284.0, 289.0, 288.0, 292.0, 295.0, 294.0], 'Neutrons': [0.0, 2.0, 4.0, 5.0, 6.0, 6.0, 7.0, 8.0, 10.0, 10.0, 12.0, 12.0, 14.0, 14.0, 16.0, 16.0, 18.0, 22.0, 20.0, 20.0, 24.0, 26.0, 28.0, 28.0, 30.0, 30.0, 32.0, 31.0, 35.0, 35.0, 39.0, 41.0, 42.0, 45.0, 45.0, 48.0, 48.0, 50.0, 50.0, 51.0, 52.0, 54.0, 55.0, 57.0, 58.0, 60.0, 61.0, 64.0, 66.0, 69.0, 71.0, 76.0, 74.0, 77.0, 78.0, 81.0, 82.0, 82.0, 82.0, 84.0, 84.0, 88.0, 89.0, 93.0, 94.0, 97.0, 98.0, 99.0, 100.0, 103.0, 104.0, 106.0, 108.0, 110.0, 111.0, 114.0, 115.0, 117.0, 118.0, 121.0, 123.0, 125.0, 126.0, 126.0, 125.0, 136.0, 136.0, 138.0, 138.0, 142.0, 140.0, 146.0, 144.0, 150.0, 148.0, 151.0, 150.0, 153.0, 153.0, 157.0, 157.0, 157.0, 159.0, 157.0, 157.0, 160.0, 157.0, 159.0, 159.0, 161.0, 161.0, 173.0, 171.0, 175.0, 173.0, 176.0, 178.0, 176.0], 
    'Protons': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0, 110.0, 111.0, 112.0, 113.0, 114.0, 115.0, 116.0, 117.0, 118.0], 
    'Electrons': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0, 110.0, 111.0, 112.0, 113.0, 114.0, 115.0, 116.0, 117.0, 118.0], 'Period': [1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0], 'Group': [1.0, 18.0, 1.0, 2.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 1.0, 2.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0], 
    'MeltingPoint': [14.175, 'Unknown', 453.85, 1560.15, 2573.15, 3948.15, 63.29, 50.5, 53.63, 24.703, 371.15, 923.15, 933.4, 1683.15, 317.25, 388.51, 172.31, 83.96, 336.5, 1112.15, 1812.15, 1933.15, 2175.15, 2130.15, 1519.15, 1808.15, 1768.15, 1726.15, 1357.75, 692.88, 302.91, 1211.45, 1090.15, 494.15, 266.05, 115.93, 312.79, 1042.15, 1799.15, 2125.15, 2741.15, 2890.15, 2473.15, 2523.15, 2239.15, 1825.15, 1234.15, 594.33, 429.91, 505.21, 904.05, 722.8, 386.65, 161.45, 301.7, 1002.15, 1193.15, 1071.15, 1204.15, 1289.15, 1204.15, 1345.15, 1095.15, 1585.15, 1630.15, 1680.15, 1743.15, 1795.15, 1818.15, 1097.15, 1936.15, 2500.15, 3269.15, 3680.15, 3453.15, 3300.15, 2716.15, 2045.15, 1337.73, 234.43, 577.15, 600.75, 544.67, 527.15, 575.15, 202.15, 300.15, 973.15, 1323.15, 2028.15, 1873.15, 1405.15, 913.15, 913.15, 1267.15, 1340.15, 1259.15, 1925.15, 1133.15, 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown'], 
    'BoilingPoint': [20.28, 4.22, 1615.0, 2742.0, 4200.0, 4300.0, 77.36, 90.2, 85.03, 27.07, 1156.0, 1363.0, 2792.0, 3538.0, 553.0, 717.8, 239.11, 87.3, 1032.0, 1757.0, 3109.0, 3560.0, 3680.0, 2944.0, 2334.0, 3134.0, 3200.0, 3186.0, 2835.0, 1180.0, 2477.0, 3106.0, 887.0, 958.0, 332.0, 119.93, 961.0, 1655.0, 3609.0, 4682.0, 5017.0, 4912.0, 5150.0, 4423.0, 3968.0, 3236.0, 2435.0, 1040.0, 2345.0, 2875.0, 1860.0, 1261.0, 457.4, 165.03, 944.0, 2170.0, 3737.0, 3716.0, 3793.0, 3347.0, 3273.0, 2067.0, 1802.0, 3546.0, 3503.0, 2840.0, 2993.0, 3503.0, 2223.0, 1469.0, 3675.0, 4876.0, 5731.0, 5828.0, 5869.0, 5285.0, 4701.0, 4098.0, 3129.0, 630.0, 1746.0, 2022.0, 1837.0, 1235.0, 610.0, 211.3, 950.0, 2010.0, 3471.0, 5061.0, 4300.0, 4404.0, 4273.0, 3501.0, 2880.0, 3383.0, 983.0, 1173.0, 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown'], 
    'Config': ['1s1', '1s2', '[He] 2s1', '[He] 2s2', '[He] 2s2 2p1', '[He] 2s2 2p2', '[He] 2s2 2p3', '[He] 2s2 2p4', '[He] 2s2 2p5', '[He] 2s2 2p6', '[Ne] 3s1', '[Ne] 3s2', '[Ne] 3s2 3p1', '[Ne] 3s2 3p2', '[Ne] 3s2 3p3', '[Ne] 3s2 3p4', '[Ne] 3s2 3p5', '[Ne] 3s2 3p6', '[Ar] 4s1', '[Ar] 4s2', '[Ar] 3d1 4s2', '[Ar] 3d2 4s2', '[Ar] 3d3 4s2', '[Ar] 3d5 4s1', 0.0, '[Ar] 3d6 4s2', '[Ar] 3d7 4s2', '[Ar] 3d8 4s2', '[Ar] 3d10 4s1', '[Ar] 3d10 4s2', '[Ar] 3d10 4s2 4p1', '[Ar] 3d10 4s2 4p2', '[Ar] 3d10 4s2 4p3', '[Ar] 3d10 4s2 4p4', '[Ar] 3d10 4s2 4p5', '[Ar] 3d10 4s2 4p6', '[Kr] 5s1', '[Kr] 5s2', '[Kr] 4d1 5s2', '[Kr] 4d2 5s2', '[Kr] 4d4 5s1', '[Kr] 4d5 5s1', '[Kr] 4d5 5s2', '[Kr] 4d7 5s1', '[Kr] 4d8 5s1', '[Kr] 4d10', '[Kr] 4d10 5s1', '[Kr] 4d10 5s2', '[Kr] 4d10 5s2 5p1', '[Kr] 4d10 5s2 5p2', '[Kr] 4d10 5s2 5p3', '[Kr] 4d10 5s2 5p4', '[Kr] 4d10 5s2 5p5', '[Kr] 4d10 5s2 5p6', '[Xe] 6s1', '[Xe] 6s2', '[Xe] 5d1 6s2', '[Xe] 4f1 5d1 6s2', '[Xe] 4f3 6s2', '[Xe] 4f4 6s2', '[Xe] 4f5 6s2', '[Xe] 4f6 6s2', '[Xe] 4f7 6s2', '[Xe] 4f7 5d1 6s2', '[Xe] 4f9 6s2', '[Xe] 4f10 6s2', '[Xe] 4f11 6s2', '[Xe] 4f12 6s2', '[Xe] 4f13 6s2', '[Xe] 4f14 6s2', '[Xe] 4f14 5d1 6s2', '[Xe] 4f14 5d2 6s2', '[Xe] 4f14 5d3 6s2', '[Xe] 4f14 5d4 6s2', 6.0, '[Xe] 4f14 5d6 6s2', '[Xe] 4f14 5d7 6s2', '[Xe] 4f14 5d9 6s1', '[Xe] 4f14 5d10 6s1', '[Xe] 4f14 5d10 6s2', '[Xe] 4f14 5d10 6s2 6p1', '[Xe] 4f14 5d10 6s2 6p2', '[Xe] 4f14 5d10 6s2 6p3', '[Xe] 4f14 5d10 6s2 6p4', '[Xe] 4f14 5d10 6s2 6p5', '[Xe] 4f14 5d10 6s2 6p6', '[Rn] 7s1', '[Rn] 7s2', '[Rn] 6d1 7s2', '[Rn] 6d2 7s2', '[Rn] 5f2 6d1 7s2', '[Rn] 5f3 6d1 7s2', '[Rn] 5f4 6d1 7s2', '[Rn] 5f6 7s2', '[Rn] 5f7 7s2', '[Rn] 5f7 6d1 7s2', '[Rn] 5f9 7s2', '[Rn] 5f10 7s2', '[Rn] 5f11 7s2', '[Rn] 5f12 7s2', '[Rn] 5f13 7s2', '[Rn] 5f14 7s2', '[Rn] 5f14 7s2 7p1', '[Rn] 5f14 6d2 7s2', '[Rn] 5f14 6d3 7s2', '[Rn] 5f14 6d4 7s2', '[Rn] 5f14 6d5 7s2', '[Rn] 5f14 6d6 7s2', 7.0, '[Rn] 5f14 6d9 7s1', '[Rn] 5f14 6d10 7s1', '[Rn] 5f14 6d10 7s2', '[Rn] 5f14 6d10 7s2 7p1', '[Rn] 5f14 6d10 7s2 7p2', '[Rn] 5f14 6d10 7s2 7p3', '[Rn] 5f14 6d10 7s2 7p4', '[Rn] 5f14 6d10 7s2 7p5', '[Rn] 5f14 6d10 7s2 7p6']
    }
global ELEMENTDATA
ELEMENTDATA=saved 
def is_float(n):
    try:
        float(n)
        return True
    except:
        return False
def parse(name):
    data=[i.split(",") for i in name.split("\n")]
    return data
def get_elements(data):
    parsed={}
    thingsiwant=["AtomicNumber","Element","AtomicMass","Neutrons","Neutrons","Protons","Electrons","Period","Group","Phase", "MeltingPoint","BoilingPoint","Config","Symbol"]
    for i in range(len(data[0])):
        if data[0][i] in thingsiwant:
            parsed[data[0][i]]=[]
            for j in data[1:]:
                if is_float(j[i]):
                    parsed[data[0][i]].append(float(j[i]))
                else:
                    parsed[data[0][i]].append(j[i])
    return parsed

    
def search(st):
    if st=="":
        return []
    # cool stuff P## to search protons E## to search electrons N## to search neutrons
    global ELEMENTDATA
    data=ELEMENTDATA
    print(ELEMENTDATA)
    print(len(st))
    if len(st)>5 and st[0]=="P" and is_float(st[1:]):
        st=st[1:]
        possible=[]
        l=data["Protons"]
        for i in range(len(l)):
            if float(st) == l[i]:
                possible.append(i)
        return possible
    elif len(st)>1 and st[0]=="E" and is_float(st[1:]):
        st=st[1:]
        possible=[]
        l=data["Electrons"]
        for i in range(len(l)):
            if float(st) == l[i]:
                possible.append(i)
        return possible
    elif len(st)>1 and st[0]=="N" and is_float(st[1:]):
        st=st[1:]
        possible=[]
        l=data["Neutrons"]
        for i in range(len(l)):
            if float(st) == l[i]:
                possible.append(i)
        return possible
    elif is_float(st):
        #assume is checking for mass number
        possible=[]
        l=data["AtomicNumber"]
        for i in range(len(l)):
            if float(st) == l[i]:
                possible.append(i)
        return possible

    elif [i for i in ['solid', 'liquid', 'gas','artificial'] if(i in st.lower())]:
        st=st[1:]
        possible=[]
        l=data["Phase"]
        for i in range(len(l)):
            if float(st) == l[i]:
                possible.append(i)
        return possible
        
    #elif "," in st:
        # assume checking for electronic configuration
        # not sure how to check
        #return chemlib.PeriodicTable.getElementByElectronicConfiguration((st.replace(" ","")).split(","))
    elif len(st)<3:
        # assume checking for symbol
        print("symbol")
        possible=[]
        l=data["Symbol"]
        #best match
        for i in range(len(l)):
            if st.lower() == l[i].lower():
                possible.append(i)
        #possible matches
        for i in range(len(l)):
            if st.lower() in l[i].lower() and i not in possible:
                possible.append(i)
        return possible
    else:
        #assume check by name
        possible=[]
        l=data["Element"]
        #best match
        for i in range(len(l)):
            if st.lower() == l[i].lower():
                possible.append(i)
        #possible matches
        for i in range(len(l)):
            if st.lower() in l[i].lower() and i not in possible:
                possible.append(i)
        return possible


if __name__=="__main__":

    # data=parse(stolendatafromchemlib)
    # data=get_elements(data)
    # print(data)
    print(search("C"))
    print(search("P12"))
    print(search("N12"))
    print(search("E12"))
    print(search("carb"))
    # print(search("solid"))