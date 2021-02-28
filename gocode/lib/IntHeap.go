package lib

// IntHeap that implement container/heap interface
type IntHeap []int

func (h IntHeap) Len() int { return len(h) }

func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }

func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

// Push item to heap
func (h *IntHeap) Push(i interface{}) { *h = append(*h, i.(int)) }

// Pop last item from heap
func (h *IntHeap) Pop() interface{} {
	last := (*h)[len(*h)-1]
	*h = (*h)[0 : len(*h)-1]
	return last
}
