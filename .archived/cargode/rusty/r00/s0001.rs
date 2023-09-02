use crate::Solution;

use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen = HashMap::new();
        for (i, num) in nums.iter().enumerate() {
            if let Some(&expect_index) = seen.get(num) {
                return vec![expect_index as i32, i as i32];
            }
            seen.insert(target-num, i);
        }
        vec![]
    }

    pub fn two_sum2(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen = HashMap::new();
        for (i, num) in nums.iter().enumerate() {
            match seen.get(&(target-num)) {
                Some(&pre) => return vec![pre as i32, i as i32],
                None => seen.insert(num, i),
            };
        }
        vec![]
    }
}


#[test]
fn two_sum_work() {
    let nums = vec![2, 6, 4, 9, 1];
    let e = vec![2, 3];
    let r = Solution::two_sum(nums, 13);
    assert_eq!(r, e);
}
