/*
PROBLEM DESCRIPTION:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

 */

/*

	Prime power: there is some number N for which p ^ N == PP

	needs to increment through primes
		take a prime
		multiply by itself
		until == given number
		or 
		until > given number
 */

class Euler5 {

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

	public static boolean isPrimePower( int x ) {

		boolean pp = false;
		int sqrtX = (int) Math.sqrt( x );
		
		for( int i = 2; i <= sqrtX; i++ ) {
			
			if( isAPrime( i ) ) {
				
				int j = i;
				int acc = i;
				while( j < x ) {
					
					acc = acc * i;

					if( acc == x ) {
						pp = true;
						break;
					}

					j++;
				}
			}

			if( pp )
				break;
		}

		return pp;
	}

	public static int primePower( int x ) {

		int i;
		int sqrtX = (int) Math.sqrt( x );
		boolean b = false;
		for( i = 2; i <= sqrtX; i++ ) {

			if( isAPrime( i ) ) {
				
				int j = i;
				int acc = i;
				while( j < x ) {
					
					acc = acc * i;

					if( acc == x ) {
						b = true;
						break;
					}

					j++;
				}
			}
			

			if( b ) {
				break;
			}
		}
		return i;

	}

	public static int smallestMultipleOfAllPrimes( int x ) {
		int acc = 1;
		int i = 2;

		while( i <= x ) {

			if ( isAPrime( i ) ) {
				acc = acc * i;

			} 

			else if ( isPrimePower( i ) ) {
				acc = acc * primePower( i ) ;
			}

			i++;
		}

		return acc;
	}



	public static void main( String[] args ) {

		System.out.println("The smallest multiple of all the primes from 1 to 10 is " 
							+ smallestMultipleOfAllPrimes( 20 ) + ".");

	}
}