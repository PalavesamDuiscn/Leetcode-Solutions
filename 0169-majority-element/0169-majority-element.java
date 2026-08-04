class Solution {
    public int majorityElement(int[] nums) {

        int total=nums[0];
        int count=1;

        for(int i=1;i<=nums.length-1;i++){
            if(nums[i]==total){
                count++;
            }
            else{
                count--;
            }
            if(count==0){
                total=nums[i];
                count=1;
            }
        }
        return total ;        
    }
}