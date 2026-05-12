class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (!numSet.contains(nums[i])) {
                numSet.add(nums[i]);
            } else {
                return true;
            }
        }
        return false;
    }
}