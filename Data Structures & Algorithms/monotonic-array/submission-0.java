class Solution {
    public boolean isMonotonic(int[] nums) {
        /*
            keep a diff of 0.
            if diff is negative and current diff of nums[i] and nums[j]
            is positive OR diff is positive and current diff is negative,
            return false.
            return true if loop finishes.
        */
        int diff = 0; 
        for (int j = 1; j < nums.length; j++) {
            int i = j - 1;
            int currDiff = nums[j] - nums[i];
            if (currDiff > 0 && diff < 0) {
                return false;
            }
            if (currDiff < 0 && diff > 0) {
                return false;
            }
            diff += currDiff;
        }
        return true;
    }
}