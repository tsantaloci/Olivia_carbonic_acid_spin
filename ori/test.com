***,Carbonic Acid CCSD(T)-F12/cc-pVTZ-F12
 memory, 995, m;
 nocompress;
 ANGSTROM
 geometry={
 O
 C 1 oc
 O 2 co 1 oco
 O 2 co 1 oco 3 180.0
 H 3 ho 2 hoc 1 0.0
 H 4 ho 2 hoc 1 0.0
 }
 oc= 1.210
 co= 1.343
 oco=125.655
 ho= 0.972
 hoc=105.765

 basis=cc-pVTZ-F12
 {hf,maxit=100}
 {ccsd(t)}
 {optg}
 {frequencies}

