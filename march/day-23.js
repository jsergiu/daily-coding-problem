/**
	Date: 23 March 2019

	This problem was recently asked by Google.
	Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
	For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
	Bonus: Can you do this in one pass?
 */


function sumOfTwo(k, inputArray = []) {
	const lookupArray = []
	let iter = 0;

	// Loop through input array
	while (iter < inputArray.length) {

		// Check if we already found the other term in the lookup array
		if (inputArray[iter] <= k && lookupArray[k - inputArray[iter]]) {
			return true
		}

		// Mark the value as found in the lookup array
		lookupArray[inputArray[iter]] = 1

		iter++;
	}

	return false;
}


console.log(sumOfTwo(13, [2, 5, 13, 8, 7, 12, 8]))