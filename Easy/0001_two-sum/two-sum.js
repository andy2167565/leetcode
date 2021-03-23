/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
/*======== <Solution 1> ========*/
    while (nums.length > 0) {
        let id = nums.indexOf(target - nums.pop());
        if (id >= 0) {
            return [id, nums.length];
        }
    }
    
/*======== <Solution 2> ========*/
    let memory = {};
    for (let i = 0; i < nums.length; i++) {
        // target = nums[i] + other_num
        // Check if other_num is in memory object
        if (memory[target - nums[i]] != undefined) {
            return [memory[target - nums[i]], i];
        }
        // Store other_num and its index for each round
        memory[nums[i]] = i;
    }
};
