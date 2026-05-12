class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();
        convertToMap(s, sMap);
        convertToMap(t, tMap);
        return sMap.equals(tMap);
    }
    public void convertToMap(String str, Map<Character, Integer> map) {
        for (int i = 0; i < str.length(); i++) {
            char strChar = str.charAt(i);
            if (map.containsKey(strChar)) {
                Integer originalValue = map.get(strChar);
                map.put(strChar, originalValue + 1);
            } else {
                map.put(strChar, 1);
            }
        }
    }
}
