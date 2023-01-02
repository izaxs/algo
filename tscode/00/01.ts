function twoSum(nums: number[], target: number): number[] {
    let seen = new Map<number, number>();
    for (let [index, value] of nums.entries()) {
        if (seen.has(value)) {
            return [seen.get(value)!, index];
        }
        seen.set(target-value, index);
    }
    return []
};
