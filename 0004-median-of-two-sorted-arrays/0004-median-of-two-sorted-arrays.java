class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] arr =new int[nums1.length+nums2.length];
        int i=0;
        for( i=0;i<nums1.length;i++){
                arr[i]=nums1[i];
        }
        int j=0;
        for( i=nums1.length;i<arr.length;i++){
            arr[i]=nums2[j];
            j++;
        }
        Arrays.sort(arr);

        double ans = 0;
        if(arr.length%2==0){
            ans=((double)arr[arr.length/2]+arr[arr.length/2-1])/2;
        }else{
            ans=arr[arr.length/2];
        }
        return ans;
    }
}