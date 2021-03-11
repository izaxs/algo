package util

// ListNode is the node of a linkedlist
type ListNode struct {
	Val  int
	Next *ListNode
}

// Linkerize converts a slice to a linkedlist, return the head of the linkedlist
func Linkerize(nums []int) *ListNode {
	fake := &ListNode{}
	cur := fake
	for _, v := range nums {
		(*cur).Next = &ListNode{v, nil}
		cur = (*cur).Next
	}
	return fake.Next
}

// Listize convert a linkedlist to a slice, using the head of the linkedlist
func Listize(node *ListNode) []int {
	result := []int{}
	for node != nil {
		result = append(result, node.Val)
		node = node.Next
	}
	return result
}
