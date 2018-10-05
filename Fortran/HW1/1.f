	program test_cos
	integer i, j
	real H(10,10), sum(10), max
c This is a program to find the maximum of sum
c This is a assignment for Numerical_Analysis

	count = 0
	do i = 1, 10
		do j = 1, 10
			H(i,j) = COS(i*0.7+ j + 2)/(i+j-1)
		enddo
	enddo
	do i = i, 10
		sum(i) = 0
	enddo
	
	do i = 1, 10
		do j = 1, 10
			sum(j) = sum(j) + H(i,j)
		enddo
	enddo

	max = sum(1)
	do i = 1, 10
		if (max .LT. sum(i)) then
			max = sum(i)

		endif
	enddo
    	print *, "max = ", max


	stop
	end program test_cos
