/*
PROBLEM DESCRIPTION:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

 */

/*

a < b < c

go through a
find a^2
go through b
find b^2
say c^2 = a^2 + b^2
find c 
	-> if c is not an integer ( 0 % 1 ), then we can stop right here
check if a + b + c = 1000
if not, increment b until b > 
say answer = a * b * c
return answer

 */

class Euler9 {

	public static double pythagProductThousand( ) {

		boolean found = false;
		double answer = 0;
		for(int a = 2; a < 400; a++ ){

			int sqrA = a * a;

			for( int b = a; b < 500; b++ ) {

				int sqrB = b * b;
				int sqrC = sqrA + sqrB;
				double c = Math.sqrt( sqrC );

				// if c is an integer
				if( ( c % 1 ) == 0 ) {
					if( a + b + c == 1000 ) {
						System.out.println("a is: "  + a );
						System.out.println("b is: "  + b );
						System.out.println("c is: "  + c );
						answer = a * b * c;
						found = true;
					}
				}

				if( found )
					break;

			}

			if( found )
				break;

		}
		return answer; 
	}

	public static void main( String[] args ) {
	
		System.out.println("Our answer is: " + pythagProductThousand( ) );
	}
} 