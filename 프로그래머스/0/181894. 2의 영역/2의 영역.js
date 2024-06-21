function solution(arr) {
    var answer = [];
    var two_lst = []
    if (arr.includes(2)){
        arr.forEach((element,index)=>{
        if(element===2){
            two_lst.push(index)
        }
    })
    min_idx = Math.min(...two_lst)
    max_idx = Math.max(...two_lst)
    
    answer = arr.slice(min_idx,max_idx+1)
        
    }
    else{
        answer.push(-1)
    }
    
    return answer;
}





/*
1. 2가 없는 경우는 바로 -1 리턴
2. 2가 있는 경우는 어떻게 해야할까?
- 2-1) forEach로 배열을 돌면서, index를 뽑자
- 2-2) index를 새로운 리스트에 넣어둔 뒤, 최솟값과 최댓값을 뽑자
- 2-3) arr[최솟값:최댓값] 으로 리스트 슬라이싱
*/
