class Solution {
    static int ans;
    public int solution(int[] numbers, int target) {
        ans = 0;
        backtracking(0, 0, target, numbers);
        return ans;
    }
    
    static void backtracking(int index, int score, int target, int[] numbers){
        if(index == numbers.length){
            if(score == target){
                ans++;
            }
            return;
        }
        
        // 현재 숫자를 더하는 경우
        backtracking(index + 1, score + numbers[index], target, numbers);
        // 현재 숫자를 빼는 경우
        backtracking(index + 1, score - numbers[index], target, numbers);
    }
}
