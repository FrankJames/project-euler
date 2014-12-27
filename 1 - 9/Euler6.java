/*
PROBLEM DESCRIPTION:

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

 */

class Euler6 {

	public static int diffSumSquares( int max ) {
		int acc = 0;
		int bcc = 0;

		// first find the sum of all squares
		for( int j = 1; j <= max; j++ ) {
			acc += j;
		}
		acc *= acc;

		// then find the square of the sum
		for( int i = 1; i <= max; i++ ) {
			bcc = bcc + ( i * i );
		}


		int diff = acc - bcc;
		return diff;

	}

	public static void main( String[] args ) {

		System.out.println("Our answer is: " + diffSumSquares( 100 ) );

	}
}