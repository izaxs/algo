package gocode

func twoSum(nums []int, target int) []int {
	wanted := make(map[int]int)
	println(wanted[1000])
	for i, v := range nums {
		w, ok := wanted[v]
		if ok {
			return []int{w, i}
		}
		wanted[target-v] = i
	}
	return nil
}
