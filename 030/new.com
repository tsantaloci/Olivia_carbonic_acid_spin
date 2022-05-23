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
 H 4 ho 2 hoc 1 30.0
}
 oc= 1.20456374
 co= 1.33807754
 oco=125.71940157
 ho= 0.96539172
 hoc=105.87929761

 basis=apVTZ
 hf,orbprint=75,maxit=100;wf,charge=0,spin=0;accu,20
 orbital,ignore_error;
 {ccsd
 eom,2.1,3.1,4.1,1.2,2.2,3.2,1.3,2.3,1.3,2.3,1.4,2.4,trans=1}
