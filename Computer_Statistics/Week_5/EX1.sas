DATA HFISH;
	SET SASHELP.FISH;
	KEEP HEIGHT;
	
PROC MEANS DATA=HFISH MAX MIN;

PROC UNIVARIATE DATA=hfish NOPRINT;
	HISTOGRAM HEIGHT
	/ NORMAL;
	
RUN;