/*
PROBLEM DESCRIPTION

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

 */

/*

19 digits is currently the cut off amount for how large we can compute
there must be a way to solve this problem going to 1000 digits.

 */


class Euler25 {

	public static int firstfibWithXDigits( int x ) {
		boolean flip = true;
		int term = 2;
		long fib = 0;
		long first = 1;
		long second = 1;
		double constraint = Math.pow(10,(x-1));

		while( fib < constraint ) {
			fib = first + second;
			term++;

			if( flip ) {
				first = fib;
				flip = false;
			}
			else {
				second = fib;
				flip = true;
			}
		}

		return term;

	}

	public static void main( String[] args ) {
		System.out.println("Our answer is: " + firstfibWithXDigits( 19 ) );
	}
	
}