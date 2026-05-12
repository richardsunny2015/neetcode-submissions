class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> scores = new Stack<>();
        for (int i = 0; i < operations.length; i++) {
            String op = operations[i];
            if (op.equals("C")) {
                scores.pop();
            } else if (op.equals("+")) {
                int lastScore = scores.pop();
                int secondToLastScore = scores.pop();
                int newScore = lastScore + secondToLastScore;
                scores.add(secondToLastScore);
                scores.add(lastScore);
                scores.add(newScore);
            } else if (op.equals("D")) {
                int lastScore = scores.peek();
                int newScore = lastScore * 2;
                scores.add(newScore);
            } else {
                int newScore = Integer.parseInt(op);
                scores.add(newScore);
            }
        }
        return sumStack(scores);
    }
    public int sumStack(Stack<Integer> s) {
        int sum = 0;
        while (!s.isEmpty()) {
            int n = s.pop();
            sum += n;
        }
        return sum;
    }
}