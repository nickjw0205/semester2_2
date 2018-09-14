DATA class_score
	INFILE = "/R_practice/lec_note/class_score.txt" DELMITER=" " FIRSTOBS=2;
	INPUT class$ name$ kor$ eng$ mat$ sci
RUN;
	