      program prime
      integer i, j

c This is a program to find prime.
c i for prime, j for division.
c This is a assignment for Numerical_Analysis
      print *,"start to find prime between 1 and 300"
      do i = 2, 300
            do j = 2, i
                  if (mod(i,j) == 0) exit
            ENDDO
            if (i == j) then
                        print *,i 
            endif
      ENDDO
      stop
      end program prime
