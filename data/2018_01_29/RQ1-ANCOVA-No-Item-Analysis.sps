* Encoding: UTF-8.

USE ALL. 
COMPUTE filter_$=(Skipper ~=1). 
VARIABLE LABELS filter_$ 'Skipper ~=1 (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE.

UNIANOVA PostTest BY Experimental 
  /METHOD=SSTYPE(3) 
  /INTERCEPT=INCLUDE 
  /EMMEANS=TABLES(Experimental) 
  /PRINT=ETASQ DESCRIPTIVE HOMOGENEITY OPOWER 
  /CRITERIA=ALPHA(.05) 
  /DESIGN=Experimental.

UNIANOVA PostTest BY Experimental WITH PreTest 
  /METHOD=SSTYPE(3) 
  /INTERCEPT=INCLUDE 
  /EMMEANS=TABLES(Experimental) WITH(PreTest=MEAN) 
  /PRINT=ETASQ DESCRIPTIVE HOMOGENEITY OPOWER 
  /CRITERIA=ALPHA(.05) 
  /DESIGN=Experimental PreTest Experimental*PreTest.

UNIANOVA PostTest BY Experimental WITH PreTest 
  /METHOD=SSTYPE(3) 
  /INTERCEPT=INCLUDE 
  /EMMEANS=TABLES(Experimental) WITH(PreTest=MEAN) 
  /PRINT=ETASQ DESCRIPTIVE HOMOGENEITY OPOWER 
  /CRITERIA=ALPHA(.05) 
  /DESIGN=PreTest Experimental.
