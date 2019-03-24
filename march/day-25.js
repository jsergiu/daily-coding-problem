/*
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?


Sollution 1: Use the previous result to generate the next one
[
	b * c * d, = T1
	a * c * d, = T2 = (T1 / b) * a
	a * b * d, = T3 = (T2 / c) * b
	a * b * c, = T4 = (T3 / d) * c
]

Sollution 2: First generate the products under the matrxi diagonal, then the ones above the main diagonal

[1 * b * c * d * e] => 1 * bcde
[a * 1 * c * d * e] => a * cde
[a * b * 1 * d * e] => ab * de
[a * b * c * 1 * e] => abc * e
[a * b * c * d * 1] => abcd * 1

*/

// Solution 1
const multiply1 = (inputArray = []) => {
	const result = [1]
	
	for (let i = 1; i < inputArray.length; i++) {
		result[0] = result[0] * inputArray[i]
	}

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

	for (let i = 1; i < len; i++) {
		result[i] = result[i - 1] * inputArray[i - 1] 
	}

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
