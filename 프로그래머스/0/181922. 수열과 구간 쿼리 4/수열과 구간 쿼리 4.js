function solution(arr, queries) {
    var answer = [];
    for (let i = 0; i<queries.length; i++){
       [s,e,k] = queries[i];
        for (let j = s; j<=e;j++){
            if (j%k === 0){
                arr[j]+=1
            }
        }
    
    }
    answer = arr
    return answer;
}

//1. s<= i <= e인 i를 뽑아낸다. i=0,1,2,3,4
//1-1) 뽑아내는 방법:이중 for문? i,j인덱스 뽑아내기/ 구조분해할당?
//2. i와 k를 비교해서, 배수인지 본다.
//2-1) i가 k의 배수라면, i%k === 0
//3. 배수였다면, arr[i] +=1

