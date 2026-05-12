class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> result = new HashMap<>();
        for (String s : strs) {
            int[] counts = new int[26];
            for (Character c : s.toCharArray()) {
                counts[c - 'a']++;
            }
            String key = Arrays.toString(counts);
            result.putIfAbsent(key, new ArrayList<>());
            result.get(key).add(s);
        }
        return new ArrayList(result.values());
    }
   
}
