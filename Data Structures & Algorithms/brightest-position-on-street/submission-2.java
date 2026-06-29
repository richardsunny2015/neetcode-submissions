class Solution {
    public int brightestPosition(int[][] lights) {
        Map<Integer, Integer> brightness = new TreeMap<>();
        int maxBrightness = 0;
        int brightestPosition = 0;
        int curr = 0;
        for (int[] l : lights) {
            int start = l[0] - l[1], end = l[0] + l[1];
            brightness.merge(start, 1, Integer::sum);
            brightness.merge(end + 1, -1, Integer::sum);

        }
        for (Map.Entry<Integer, Integer> set : brightness.entrySet()) {
            curr += set.getValue();
            if (curr > maxBrightness) {
                maxBrightness = curr;
                brightestPosition = set.getKey();
            }
        }
        return brightestPosition;
    }
}
