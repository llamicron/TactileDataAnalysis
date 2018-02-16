* Encoding: UTF-8.
*MANOVA RQ4 TA, I, and ER vs Traintotal and TrainTotalSquared.
USE ALL. 
COMPUTE filter_$=(Skipper = 0  & Experimental = 1). 
VARIABLE LABELS filter_$ 'Skipper = 0  & Experimental = 1 (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE.
GLM TrainTotal TrainTotalSquared WITH I TA ER 
  /METHOD=SSTYPE(3) 
  /INTERCEPT=INCLUDE 
  /PRINT=DESCRIPTIVE ETASQ OPOWER 
  /CRITERIA=ALPHA(.05) 
  /DESIGN=I TA ER I*TA ER*TA ER*I ER*I*TA.

