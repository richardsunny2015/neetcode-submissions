class Solution {
    public String simplifyPath(String path) {
        // replace all multi-slashes with just /
        /*  keep a pointer (start at -1).
            if the path is a valid path name,
            append the path, increment pointer.
            if it is '..', decrement pointer
            if it is '.', do nothing?
            at the end, loop from 0 to pointer inclusive
            and create file path.
        */
        Stack<String> dir = new Stack<>();
        String singleSlashes = path.replaceAll("/+", "/");
        String[] splitStr = singleSlashes.split("/");
        System.out.println(splitStr[0]);
        for (int i = 0; i < splitStr.length; i++) {
            if (splitStr[i].equals("..")) {
                if (dir.size() > 0) {
                    dir.pop();
                }
            } else if (!splitStr[i].equals(".")) {
                dir.push(splitStr[i]);
            }
        }
        String returnVal = String.join("/", dir);
        return returnVal.startsWith("/") ? returnVal : "/" + returnVal;
    }
}