/*
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the
next node and the previous node.
Implement an XOR linked list; it has an add(element)
which adds the element to the end, and a get(index)
which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer
functions that converts between nodes and memory addresses.

*/

class Node {
	constructor(value) {
		this.value = value
		this.next = null
	}
}

class XorLinkedList {

	constructor() {
		this.head = this.tail = null
	}

	add(value) {
		const node = new Node(value)

		if (this.head === null) {
			this.head = this.tail = node
		} else {
			this.tail.next = node
			this.tail = node 
		}
	}

	get(index) {
		let i = 0;
		let node = this.head

		while (i < index) {
			node = node.next
			i++
		}

		return node
	}

}

const graph = new XorLinkedList()
graph.add(1)
graph.add(2)
graph.add(3)


console.log(graph.get(2))