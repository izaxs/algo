package util

import (
	"testing"
)

func Test_Linkerize(t *testing.T) {
	nums := []int{1, 2, 3}
	result := Linkerize(nums)
	node3 := &ListNode{Val: 3}
	node2 := &ListNode{2, node3}
	node1 := &ListNode{1, node2}
	AssertSameLinkedList(t, node1, result)
}

func Test_Listize(t *testing.T) {
	node3 := &ListNode{Val: 3}
	node2 := &ListNode{2, node3}
	node1 := &ListNode{1, node2}
	result := Listize(node1)
	expected := []int{1, 2, 3}
	AssertSameIntSlice(t, expected, result)
}
