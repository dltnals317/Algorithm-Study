function solution(arr) {
    var stk = [];
    var i = 0
    while(i<arr.length){
        if(stk.length ===0){
            stk.push(arr[i])
            i++
        }
        else{
            if (stk[stk.length -1] < arr[i]){
                stk.push(arr[i])
                i++
            }
            else{
                stk.pop()
            }
            
        }
    }
    return stk;
}


/*
그냥 조건문 잘 활용하면 되는 문제인듯

1. stk가 빈 배열 -> arr[i]를 stk에 추가 & i에 1 더함
2. stk가 안 빈 배열
    - 2.a)stk의 마지막 원소 < arr[i] :  arr[i]를 stk의 뒤에 추가 & i에 1을 더함
    - 2.b)stk의 마지막 원소 >= arr[i] : stk의 마지막 원소를 stk에서 제거

*/