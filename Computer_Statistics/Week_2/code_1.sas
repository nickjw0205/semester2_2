DATA SCORE1;
	INFILE "/folders/myshortcuts/R_practice/Week_2/score1.txt";
	INPUT GENDER$ KOR MAT ENG SCI;
	
DATA SCORE2;
	INFILE "/folders/myshortcuts/R_practice/Week_2/score2.txt";
	INPUT GENDER$ KOR MAT ENG SCI;
	
DATA SCORE;
	SET SCORE1 SCORE2;
	
DATA PASS;
	INFILE "/folders/myshortcuts/R_practice/Week_2/pass.txt"
	LENGTH PASS$ 9;
	INPUT GENDER$ PASS$;
	
DATA SCORE_PASS;
	MERGE SCORES PASS;
	
RUN;