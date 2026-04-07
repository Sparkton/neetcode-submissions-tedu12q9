class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    binary_search(nums, target, l, r) {
        if ( l > r ) return -1;
        let  m = l + Math.floor((r-l)/2)
        if (nums[m] === target) return m;
        return (nums[m] < target) ?
            this.binary_search(nums, target, m+1, r) :
            this.binary_search(nums, target, l, m-1);
    }

    search(nums, target) {
        return this.binary_search(nums, target, 0, nums.length - 1);
    }
}