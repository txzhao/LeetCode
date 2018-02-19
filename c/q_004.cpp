double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int res[nums1Size + nums2Size];
    int i = 0, j = 0, count = 0;
    
    // merge two arrays ascendingly
    while (i < nums1Size || j < nums2Size) {
        if (i >= nums1Size && j < nums2Size) {
            res[count] = *(nums2+j); 
            j++;
        }
        
        if (j >= nums2Size && i < nums1Size) {
            res[count] = *(nums1+i); 
            i++;
        }
        
        if (i < nums1Size && j < nums2Size) {
            if (*(nums1+i) < *(nums2+j)) {
                res[count] = *(nums1+i); 
                i++;
            }
            else {
                res[count] = *(nums2+j); 
                j++;
            }
        } 
        count++;
    }
    
    // calculate median
    if ((nums1Size+nums2Size)%2==0) {
        int idx = (nums1Size+nums2Size-1)/2;
        return (res[idx] + res[idx+1])/2.0;
    }
    else return (float) res[(nums1Size+nums2Size)/2];
}