/*
PROBLEM DESCRIPTION:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

 */
/*

start counter at 0
whenever we find a prime,
we increase our counter

we don't know what our end result will be

 */

class Euler7 {

	public static boolean isAPrime( int x ) {

		boolean prime = true;

		for( int i = 2; i <= Math.sqrt( x ); i++ ) {
			if ( ( x % i ) == 0 ) {
				prime = false;
				break;
			}
		}

		return prime;
	}

	public static int primeNumber( int index ) {
		int counter = 0;
		int j = 1; 
		while( counter < index ) {
			j++;

			if( isAPrime( j ) ) {
				counter++;
			}

			
		}
		return j;

	}

	public static void main( String[] args ) {
		System.out.println("Our answer is: " + primeNumber( 10001 ) );
	}
}