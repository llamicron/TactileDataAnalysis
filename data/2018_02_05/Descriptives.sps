* Encoding: UTF-8.
*Descriptives post-skipper.
USE ALL. 
COMPUTE filter_$=(Skipper = 0). 
VARIABLE LABELS filter_$ 'Skipper = 0 (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE. 
DESCRIPTIVES VARIABLES=PreTest PreTestIA PostTest PostTestIA NavTotal TrainTotal SR RE I TA ER 
  /STATISTICS=MEAN STDDEV MIN MAX KURTOSIS SKEWNESS.
