DATA CARS;
	SET SASHELP.CARS;

PROC CORR DATA=CARS;
	VAR HORSEPOWER LENGTH;
RUN;