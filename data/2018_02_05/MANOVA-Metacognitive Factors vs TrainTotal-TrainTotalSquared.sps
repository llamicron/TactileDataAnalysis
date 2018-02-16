* Encoding: UTF-8.
*MANOVA SR and RE vs Traintotal and TrainTotalSquared.
USE ALL. 
COMPUTE filter_$=(Skipper = 0  & Experimental = 1). 
VARIABLE LABELS filter_$ 'Skipper = 0  & Experimental = 1 (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE.
GLM TrainTotal TrainTotalSquared WITH SR RE 
  /METHOD=SSTYPE(3) 
  /INTERCEPT=INCLUDE 
  /PRINT=DESCRIPTIVE ETASQ OPOWER 
  /CRITERIA=ALPHA(.05) 
  /DESIGN=SR RE RE*SR.
