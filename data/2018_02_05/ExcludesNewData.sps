* Encoding: UTF-8.
USE ALL. 
COMPUTE filter_$=(P1StartDate < date.mdy(12,31,17)). 
VARIABLE LABELS filter_$ 'P1StartDate < date.mdy(12,31,17) (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE.
