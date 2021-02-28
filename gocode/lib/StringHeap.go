package lib

// StringHeap that implement container/heap interface
type StringHeap []string

func (h StringHeap) Len() int { return len(h) }

func (h StringHeap) Less(i, j int) bool { return h[i] < h[j] }

func (h StringHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

// Push item to heap
func (h *StringHeap) Push(i interface{}) { *h = append(*h, i.(string)) }

// Pop last item from heap
func (h *StringHeap) Pop() interface{} {
	last := (*h)[len(*h)-1]
	*h = (*h)[0 : len(*h)-1]
	return last
}
