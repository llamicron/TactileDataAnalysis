* Encoding: UTF-8.

USE ALL. 
COMPUTE filter_$=(Skipper ~=1). 
VARIABLE LABELS filter_$ 'Skipper ~=1 (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE.

  RELIABILITY 
  /VARIABLES=PostQ1 PostQ2 PostQ3 PostQ4 PostQ5 PostQ6 PostQ7 PostQ8 PostQ9 PostQ10 PostQ11 PostQ12 
    PostQ13 PostQ14 PostQ15 PostQ16 PostQ17 PostQ18 PostQ19 PostQ20 
  /SCALE('ALL VARIABLES') ALL 
  /MODEL=ALPHA 
  /STATISTICS=DESCRIPTIVE SCALE CORR 
  /SUMMARY=TOTAL.


  RELIABILITY 
  /VARIABLES=PostQ1 PostQ3 PostQ5 PostQ6 PostQ9 PostQ10 PostQ11 PostQ12 
    PostQ14 PostQ16 PostQ17 PostQ18 PostQ19 PostQ20 
  /SCALE('ALL VARIABLES') ALL 
  /MODEL=ALPHA 
  /STATISTICS=DESCRIPTIVE SCALE CORR 
  /SUMMARY=TOTAL.

COMPUTE PostTestIA=PostQ1 + PostQ3 + PostQ5 + PostQ6 + PostQ9 + PostQ10 + PostQ11 + PostQ12 
    + PostQ14 + PostQ16 + PostQ17 + PostQ18 + PostQ19 + PostQ20 . 
EXECUTE.

