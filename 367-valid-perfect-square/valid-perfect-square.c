bool isPerfectSquare(int num) {
    long left = 1;
    long right = num;
    while(left<right){
        long mid = left + (right - left)/2;
        if(mid*mid==num){
            return true;
        }else if (mid*mid>num){
            right = mid;
        }else{
            left = mid + 1;
        }
    }
    return left*right == num;
}