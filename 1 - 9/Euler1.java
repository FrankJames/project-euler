/*
PROBLEM DESCRIPTION:

"If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.""

 */

class Euler1 {
	int maxNumber;

	public Euler1( int x ) {
		this.maxNumber = x;
	}

	public int multiplesOfThreeAndFive( ) {

		int acc = 0;

		for( int i = 0; i < maxNumber; i++ ) {

			if( ( ( i % 5 ) == 0 ) && ( ( i % 3 ) == 0 ) ) {
				acc = acc + i;
			} else if ( ( i % 5 ) == 0 ) {
				acc = acc + i;
			} else if ( ( i % 3 ) == 0 ) {
				acc = acc + i;
			}

		}

		return acc;
	}

	public static void main( String[] args ) {

		Euler1 e = new Euler1( 1000 );
		int num = e.multiplesOfThreeAndFive( );
		System.out.println("Our answer should be " + num );

	}
}