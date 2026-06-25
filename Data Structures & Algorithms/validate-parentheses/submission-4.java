class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Set<Character> opens = new TreeSet<>();
        opens.add('(');
        opens.add('{');
        opens.add('[');
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if (opens.contains(c)) {
                stack.push(c);
            } else if (c.equals(')')) {
                if (stack.size() < 1 || !stack.pop().equals('(')) {
                    return false;
                }
            } else if (c.equals('}')) {
                if (stack.size() < 1 || !stack.pop().equals('{')) {
                    return false;
                }
            } else if (c.equals(']')) {
                if (stack.size() < 1 || !stack.pop().equals('[')) {
                    return false;
                }
            }
        }
        return stack.size() == 0;
    }
}
