      program prime
      integer i, j, count

c This is a program to find prime.
c i for prime, j for division.
c This is a assignment for Numerical_Analysis
      print *,"start to find 300th prime"
      count = 0
      i = 2
	do while (count .NE. 300)
		do j = 2, i
                  if (mod(i,j) == 0) exit
            
            ENDDO
            if (i == j) then
                        count = count + 1
            endif
            i = i + 1

    	ENDDO
    	print *, i-1
      stop
      end program prime
