class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hMap = new HashMap<>();
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            int diff = target - current;
            if (hMap.containsKey(diff)) {
                result[0] = hMap.get(diff);
                result[1] = i;
            }
            hMap.put(current, i);
        }
        return result;
    }
}
