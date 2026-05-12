class Solution {
    public boolean isValidSudoku(char[][] board) {
        // check rows
        for (char[] row : board) {
            Set<Character> nums = new HashSet<>();
            for (char num : row) {
                if (num == '.') continue;
                if (nums.contains(num)) return false;
                nums.add(num);
            }
        }
        // check columns
        for (int i = 0; i < board.length; i++) {
            Set<Character> nums = new HashSet<>();
            for (int j = 0; j < board.length; j++) {
                char num = board[j][i];
                if (num == '.') continue;
                if (nums.contains(num)) return false;
                nums.add(num);
            }
        }
        for (int square = 0; square < board.length; square++) {
            Set<Character> nums = new HashSet<>();
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int row = (square / 3) * 3 + i;
                    int col = (square % 3) * 3 + j;
                    char num = board[row][col];
                    if (num == '.') continue;
                    if (nums.contains(num)) return false;
                    nums.add(num);
                }
            }
        }

        return true;
    }
}
