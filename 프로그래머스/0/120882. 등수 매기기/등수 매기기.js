function solution(score) {
    var answer = [];
    var average_lst = [];
    var rank = new Object()
    score.map((sc,idx)=>{
        [english,math] = sc
        average = (english + math) / 2
        average_lst.push(average)
        score[idx].push(average)
    })
   
    average_lst.sort((a, b) => b - a); //2차원 배열의 각 lst 맨 뒤값 기준으로 내림차순 정렬
    average_lst.forEach((avg,idx)=>{
        rank[idx+1] = avg
    })
    //const key = keysOfPerson.find((key) => Person[key] === 4);

    score.forEach((lst,idx)=>{
       sc = lst[lst.length-1]
       
       const keysOfScore = Object.keys(rank);

       const r = keysOfScore.find((key)=>rank[key] === sc)
       console.log("r",r)
       answer.push(parseInt(r))
    })
    
   
    return answer;
}


/*
1. 2차원 배열 score을 돌면서, 꺼낸 1차원리스트에서 구조분해 할당으로 영어,수학에 할당하고 평균구함
2. 평균 리스트에 push -> 평균 리스트 sort(내림차순 정렬)
3. 평균 리스트에서 index뽑아서, [영아,수학]에 push
4.다시 for문 돌면서, 마지막
*/