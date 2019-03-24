/*

Date: 25 March 2019

This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

Sollution 1: Use the previous result to generate the next one
>>> r[i] = r[i - 1] / input[i - 1] * input[i] 

Sollution 2: First generate the products under the matrxi diagonal, then the ones above the main diagonal
>>> r = [1, a, ab, abc, abcd] * [bcde, cde, de, e, 1]

*/

// Solution 1
const multiply1 = (inputArray = []) => {
	const result = [1]
	
	// Calculate result [0]
	for (let i = 1; i < inputArray.length; i++) {
		result[0] = result[0] * inputArray[i]
	}

	// Calculate the rest of the items 
	for (let i = 1; i < inputArray.length; i++) {
		result[i] = result[i - 1] / inputArray[i] * inputArray[i - 1]
	}

	return result
}

// Sollution 2
const multiply2 = (inputArray = []) => {
	const result = [1]
	const len = inputArray.length;
	let p = inputArray[0];

	// Multiply the numbers under the main diagonal, row by row
	for (let i = 1; i < len; i++) {
		result[i] = result[i - 1] * inputArray[i - 1] 
	}

	// Multiply the numbers above the main diagonal, row by row
	p = 1
	for (let i = len - 1; i >= 0; i--) {
		result[i] = result[i] * p;
		p = p * inputArray[i]
	}

	return result
}

console.log(multiply1([1, 2, 3, 4, 5]))
console.log(multiply1([1, 2, 3]))
console.log(multiply2([1, 2, 3, 4, 5]))
console.log(multiply2([1, 2, 3]))
