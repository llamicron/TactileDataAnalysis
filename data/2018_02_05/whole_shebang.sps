* Encoding: UTF-8.
*compare skippers to non-skippers based upon 10/5.
FILTER OFF. 
USE ALL. 
EXECUTE. 
UNIANOVA PostTest BY Skipper 
  /METHOD=SSTYPE(3) 
  /INTERCEPT=INCLUDE 
  /PRINT ETASQ DESCRIPTIVE HOMOGENEITY OPOWER 
  /CRITERIA=ALPHA(.05) 
  /DESIGN=Skipper.

*pre-test item analysis.
USE ALL. 
COMPUTE filter_$=(Skipper ~=1). 
VARIABLE LABELS filter_$ 'Skipper ~=1 (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE.
RELIABILITY 
  /VARIABLES=PreQ1 PreQ2 PreQ3 PreQ4 PreQ5 PreQ6 PreQ7 PreQ8 PreQ9 PreQ10 
  /SCALE('ALL VARIABLES') ALL 
  /MODEL=ALPHA 
  /STATISTICS=DESCRIPTIVE SCALE CORR 
  /SUMMARY=TOTAL.
RELIABILITY 
  /VARIABLES=PreQ1 PreQ2 PreQ3 PreQ4 PreQ5 PreQ6 PreQ7 PreQ8 PreQ9
  /SCALE('ALL VARIABLES') ALL 
  /MODEL=ALPHA 
  /STATISTICS=DESCRIPTIVE SCALE CORR 
  /SUMMARY=TOTAL.

*post-test item analysis.
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

*RQ1 - compare experimental and control ANCOVA.
USE ALL. 
COMPUTE filter_$=(Skipper ~=1). 
VARIABLE LABELS filter_$ 'Skipper ~=1 (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE.
UNIANOVA PostTestIA BY Experimental 
  /METHOD=SSTYPE(3) 
  /INTERCEPT=INCLUDE 
  /EMMEANS=TABLES(Experimental) 
  /PRINT=ETASQ DESCRIPTIVE HOMOGENEITY OPOWER 
  /CRITERIA=ALPHA(.05) 
  /DESIGN=Experimental.
UNIANOVA PostTestIA BY Experimental WITH PreTestIA 
  /METHOD=SSTYPE(3) 
  /INTERCEPT=INCLUDE 
  /EMMEANS=TABLES(Experimental) WITH(PreTestIA=MEAN) 
  /PRINT=ETASQ DESCRIPTIVE HOMOGENEITY OPOWER 
  /CRITERIA=ALPHA(.05) 
  /DESIGN=Experimental PreTestIA Experimental*PreTestIA.
UNIANOVA PostTestIA BY Experimental WITH PreTestIA 
  /METHOD=SSTYPE(3) 
  /INTERCEPT=INCLUDE 
  /EMMEANS=TABLES(Experimental) WITH(PreTestIA=MEAN) 
  /PRINT=ETASQ DESCRIPTIVE HOMOGENEITY OPOWER 
  /CRITERIA=ALPHA(.05) 
  /DESIGN=PreTestIA Experimental.

*RQ1.5 Does navigation use affect comprehension.
USE ALL. 
COMPUTE filter_$=(Skipper = 0  & Experimental = 1). 
VARIABLE LABELS filter_$ 'Skipper = 0  & Experimental = 1 (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE.  
* Curve Estimation. 
TSET NEWVAR=NONE. 
CURVEFIT 
  /VARIABLES=NavTotal WITH PostTestIA 
  /CONSTANT 
  /MODEL=LINEAR QUADRATIC 
  /PLOT FIT.
REGRESSION
  /MISSING LISTWISE 
  /STATISTICS COEFF OUTS R ANOVA CHANGE 
  /CRITERIA=PIN(.05) POUT(.10) 
  /NOORIGIN 
  /DEPENDENT PostTestIA 
  /METHOD=ENTER NavTotal 
  /METHOD=ENTER NavTotalSquared.

*MANOVA RQ2 SR and RE vs Navtotal and NavTotalSquared.
USE ALL. 
COMPUTE filter_$=(Skipper = 0  & Experimental = 1). 
VARIABLE LABELS filter_$ 'Skipper = 0  & Experimental = 1 (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE.
GLM TrainTotal NavTotalSquared WITH SR RE 
  /METHOD=SSTYPE(3) 
  /INTERCEPT=INCLUDE 
  /PRINT=DESCRIPTIVE ETASQ OPOWER PARAMETER 
  /CRITERIA=ALPHA(.05) 
  /DESIGN=SR RE RE*SR.



*MANOVA RQ3 TA, I, and ER vs Navtotal and NavTotalSquared.
USE ALL. 
COMPUTE filter_$=(Skipper = 0  & Experimental = 1). 
VARIABLE LABELS filter_$ 'Skipper = 0  & Experimental = 1 (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE.
GLM TrainTotal NavTotalSquared WITH I TA ER 
  /METHOD=SSTYPE(3) 
  /INTERCEPT=INCLUDE 
  /PRINT=DESCRIPTIVE ETASQ OPOWER PARAMETER 
  /CRITERIA=ALPHA(.05) 
  /DESIGN=I TA ER I*TA ER*TA ER*I ER*I*TA

