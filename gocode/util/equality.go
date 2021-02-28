package util

import "testing"

const errorTemplate = "\nExpected: %v\nGot:      %v"

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
