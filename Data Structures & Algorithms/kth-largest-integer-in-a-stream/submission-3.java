class KthLargest {
    private PriorityQueue<Integer> heap;
    private int k;
    public KthLargest(int k, int[] nums) {
        this.heap = new PriorityQueue<>();
        for (int i = 0; i < nums.length; i++) {
            heap.add(nums[i]);
        }
        this.k = k;
    }
    
    public int add(int val) {
        heap.add(val);
        while (heap.size() > k) {
            heap.poll();
        }
        return heap.peek();
    }
}
