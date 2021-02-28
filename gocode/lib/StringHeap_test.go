package lib

import (
	"container/heap"
	"testing"
)

func Test_StringHeap(t *testing.T) {
	h := &StringHeap{"Hello", "", "7"}
	heap.Init(h)
	heap.Push(h, "apple")
	heap.Push(h, "Apple")
	heap.Push(h, "World!")

	expect := []string{"", "7", "Apple", "Hello", "World!", "apple"}
	result := make([]string, 0, len(expect))
	for h.Len() > 0 {
		result = append(result, heap.Pop(h).(string))
	}

	if !IsSameStringSlice(expect, result) {
		t.Errorf("\nExpected: %v\nGot:      %v", expect, result)
	}
}
