import java.util.Arrays;

class Solution {

    public int maxArea(int[] height) {

        int left = 0;
        int right = height.length - 1;

        int maxWater = 0;

        while (left < right) {

            int width = right - left;

            int containerHeight = Math.min(
                height[left],
                height[right]
            );

            int currentWater = width * containerHeight;

            maxWater = Math.max(
                maxWater,
                currentWater
            );

            // Move the shorter side
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxWater;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int[] height1 = {1,8,6,2,5,4,8,3,7};
        System.out.println("Example 1: " + solution.maxArea(height1));  // Output: 49
        
        int[] height2 = {1,1};
        System.out.println("Example 2: " + solution.maxArea(height2));  // Output: 1
    }
}