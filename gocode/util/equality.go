package util

import "testing"

const (
	recursionLimit = 100000
	errorTemplate  = "\nExpected: %v\nGot:      %v"
)

// IsSameIntSlice checks if slices are equal
func IsSameIntSlice(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i, v := range a {
		if v != b[i] {
			return false
		}
	}
	return true
}

// AssertSameIntSlice fail the test if slices are not equal
func AssertSameIntSlice(t *testing.T, expected, result []int) {
	if !IsSameIntSlice(expected, result) {
		t.Errorf(errorTemplate, expected, result)
	}
}

// IsSameStringSlice checks if slices are equal
func IsSameStringSlice(a, b []string) bool {
	if len(a) != len(b) {
		return false
	}
	for i, v := range a {
		if v != b[i] {
			return false
		}
	}
	return true
}

// AssertSameStringSlice fail the test if slices are not equal
func AssertSameStringSlice(t *testing.T, expected, result []string) {
	if !IsSameStringSlice(expected, result) {
		t.Errorf(errorTemplate, expected, result)
	}
}

// IsSameLinkedList compares two linkedlist
func IsSameLinkedList(expected, result *ListNode) bool {
	limit := recursionLimit
	for (expected == nil) == (result == nil) && limit > 0 {
		if expected == nil {
			return true
		}
		if expected.Val != result.Val {
			return false
		}
		expected, result = expected.Next, result.Next
		limit--
	}
	return false
}

// AssertSameLinkedList fail the test if slices are not equal
func AssertSameLinkedList(t *testing.T, expected, result *ListNode) {
	if !IsSameLinkedList(expected, result) {
		t.Errorf(errorTemplate, expected, result)
	}
}
