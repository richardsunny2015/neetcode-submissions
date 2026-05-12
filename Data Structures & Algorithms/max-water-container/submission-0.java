class Solution {
    public int maxArea(int[] heights) {
        int l = 0;
        int r = heights.length - 1;
        int maxVolume = 0;
        while (l < r) {
            int leftHeight = heights[l];
            int rightHeight = heights[r];
            int minHeight = Math.min(leftHeight, rightHeight);
            int length = r - l;
            int product = minHeight * length;
            maxVolume = Math.max(maxVolume, product);
            if (leftHeight < rightHeight) l++;
            else r--;
        }
        return maxVolume;
    }
}
