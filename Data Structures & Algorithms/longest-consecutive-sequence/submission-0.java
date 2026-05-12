class Solution {
    public int longestConsecutive(int[] nums) {
        SortedSet<Integer> sortedSet = new TreeSet();
        for (int num : nums) {
            sortedSet.add(num);
        }
        Integer[] sortedNums = sortedSet.toArray(new Integer[0]);
        int longestSequence = 0;
        int currentSequence = 0;
        for (int i = 0; i < sortedNums.length; i++) {
            System.out.println(sortedNums[i]);
            if (i == 0 || sortedNums[i - 1] + 1 == sortedNums[i]) {
                currentSequence++;
            } else {
                currentSequence = 1;
            }
            longestSequence = Math.max(longestSequence, currentSequence);
        }
        return longestSequence;
    }
}
