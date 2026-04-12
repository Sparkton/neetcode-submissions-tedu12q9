impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let (mut l, mut r) = (0_usize, numbers.len() - 1);

        while l < r {
            let curr_sum = numbers[l] + numbers[r];
            if curr_sum > target {
                r -= 1;
            } else if curr_sum < target {
                l += 1
            } else {
                return vec![l as i32 + 1, r as i32 + 1];
            }
        }
        vec![]
    }
}
