/*
PROBLEM DESCRIPTION: 

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

 */

class Euler10 {

	public static boolean isAPrime( int n ) {
		boolean prime = true;

		for( int i = 2; i <= Math.sqrt( n ); i++ ) {
			if( ( n % i ) == 0 ){
				prime = false;
				break;
			}
		}

		return prime;
	}

	public static long sumPrimesTo( int max ) {
		long sum = 0;
		for( int i = 2; i <= max; i++ ) {
			if( isAPrime( i ) ) {
				sum += i;
			}
		}

		return sum;
	}


	public static void main( String[] args ) {
		System.out.println("Our answer is: " + sumPrimesTo( 2000000 ) );
	}
}