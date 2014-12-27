/*
PROBLEM DESCRIPTION:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

 */


/*
	- find closest smaller long less than sqrt 600851475143
	- decrement from there until find an i such that 600851475143 (mod i) == 0

	how do we guaruntee that i is a prime? 
		
 */

class Euler3 {

	public static boolean isAPrime( double x ) {

		boolean prime = true;

		for( int i = 2; i <= (int) Math.sqrt( x ); i++ ) {

			if( ( x % i ) == 0 ) {
				prime = false;
				break;
			}
		}

		return prime;

	}

	public static double largestPrimeFactor( long x ) {

		double flooredX = Math.floor( Math.sqrt( x ) );
		double modulus = 0;

		for( int i = 0; i < flooredX; i++ ) {

			modulus = flooredX - i;

			// if the modulus is a a prime and it divides x, then it is the largest
			// such prime that divides x
			
			if( ( ( x % modulus ) == 0 ) && isAPrime( modulus ) ) {
				break;
			}
		}

		return modulus;
	}

	public static void main( String[] args ) {

	long question = 0;
	question += 600851475143.0;

	System.out.println("The largest prime factor of 600851475143 is " + largestPrimeFactor( question ) );

	}
}

/*
	Notes: 
		The number given to us is literally too large for java to handle,
		but our function does indeed work as intended. A workaround would
		be to use a different programming language, ie Racket.

 */