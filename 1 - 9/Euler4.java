/*
PROBLEM DESCRIPTION:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

 */

/*

	Find Palindromes
	

	Notes:
		need to find: 
			how to recognise palindromic numbers
			how to find palindromic numbers
	
		perhaps:
			make a palindromic number
					-> there are either 5 or 6 digits!

			find the factors of it
				-> make sure those factors are indeed 3-digit numbers, ie 99 < X < 1000
				-> only two factors


		A palindromic number is constructed such that:
			Digit A
			Digit B
			Digit C
			...

			Number: A B C ... C B A


		Currently have every 6 digit palindrome couting down from 999999 to 100001

		now need to check if one of these palindromes divided by some three digit number
		is also a three digit number.

 */


class Euler4 {

	public static int largestPalindrome( ) {

		int palindrome = 0;
		boolean found = false;

		for( int i = 9; i >= 1; i-- ) {
			for( int j = 9; j >= 0; j-- ) {
				for( int k = 9; k >= 0; k-- ) {
					palindrome = (i * 100000) + (j * 10000) + (k * 1000)
								+ (k * 100) + (j * 10) + i;

					for( int l = 999; l > 100; l-- ) {

						if( ( palindrome % l == 0 ) && ( ( palindrome / l ) > 99 ) &&
							( 1000 > ( palindrome / l ) ) ) {
							found = true;
						}

						if (found)
							break;
					}

					if (found)
						break;
					
				}

				if (found)
					break;
			}

			if (found)
				break;
		}


		return palindrome;
	}

	public static void main( String[] args ) {

		System.out.println("Our answer is " + largestPalindrome( ) );
	}

}