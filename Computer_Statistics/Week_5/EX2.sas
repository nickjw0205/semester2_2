DATA NFISH;
	SET SASHELP.FISH;
	KEEP SPECIES;
	
PROC SGPLOT DATA=NFISH;
	VBAR SPECIES;
	TITLE "Frequency of fish specises";

RUN;