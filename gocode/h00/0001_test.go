package h00

import (
	"testing"

	"github.com/gearbird/algo/goutil"
)

func Test_twoSum(t *testing.T) {
	inputNums := []int{4, 5, 9, 1, 10, 2}
	inputTarget := 11
	expected := []int{3, 4}
	result := twoSum(inputNums, inputTarget)

	goutil.AssertSameIntSlice(t, expected, result)
}
