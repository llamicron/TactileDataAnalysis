* Encoding: UTF-8.

USE ALL. 
COMPUTE filter_$=(Skipper  ~=  1). 
VARIABLE LABELS filter_$ 'Skipper  ~=  1 (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE.

  RELIABILITY 
  /VARIABLES=PreQ1 PreQ2 PreQ3 PreQ4 PreQ5 PreQ6 PreQ7 PreQ8 PreQ9 PreQ10
  /SCALE(ALPHA)=ALL 
  /MODEL=ALPHA 
  /STATISTICS=SCALE
  /SUMMARY=TOTAL.
  
  RELIABILITY 
  /VARIABLES=PostQ1 PostQ2 PostQ3 PostQ4 PostQ5 PostQ6 PostQ7 PostQ8 PostQ9 PostQ10 
  PostQ11 PostQ12 PostQ13 PostQ14 PostQ15 PostQ16 PostQ17 PostQ18 PostQ19 PostQ20 
  /SCALE(ALPHA)=ALL 
  /MODEL=ALPHA 
  /STATISTICS=SCALE 
  /SUMMARY=TOTAL.
