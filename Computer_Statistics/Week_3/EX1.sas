DATA CLASS;
	SET SASHELP.CLASS;
	
DATA FISH;
	SET SASHELP.FISH;
	
PROC PRINT DATA=CLASS;
PROC PRINT DATA=FISH;
RUN;