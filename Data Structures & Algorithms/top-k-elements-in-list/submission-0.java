class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        int[] result = new int[k];
        List<int[]> freqs = new ArrayList<>();
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            freqs.add(new int[] {entry.getValue(), entry.getKey()});
        }
        freqs.sort((a, b) -> b[0] - a[0]);
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = freqs.get(i)[1];
        }
        return res;
    }
}
