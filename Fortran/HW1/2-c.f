      program prime
      integer i, j, count

c This is a program to find prime.
c i for prime, j for division.
c This is a assignment for Numerical_Analysis
      print *,"start to find the number of prime between 1 and 100"
      count = 0
      do i = 2, 10000
            do j = 2, i
                  if (mod(i,j) == 0) exit
            ENDDO
            if (i == j) then
                        count = count + 1
            endif
      ENDDO
      print *, count
      stop
      end program prime
