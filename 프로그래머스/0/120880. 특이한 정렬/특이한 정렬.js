function solution(numlist, n) {
    var answer = [];
    var tmp_lst = [];
    numlist.map((num)=>{
        tmp_lst.push([Math.abs(num-n),num])
    })
    
    tmp_lst.sort((a,b)=>{
        if(a[0] !==b[0]){ //거리가 같지 않으면
         return a[0]-b[0] //앞 원소(거리) 기준으로 오름차순 정렬
    }
    else{ //원소가 같다면
        return b[1]-a[1] //뒤 원소기준으로 내림차순 정렬
    }
    })
    
    tmp_lst.map((lst)=>{
       answer.push(lst[1])
    })
    console.log(tmp_lst)
    return answer;
}


/*
-기준점 n을 기준으로 i=0,1,2,3.... 로 양옆 기록하기(기록된 숫자가 numlist길이와 같아질 때까지)
- 만약 거리가 같다면, 큰 수가 앞으로 오게하기
-indexof활용

*/