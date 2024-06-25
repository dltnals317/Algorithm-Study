function solution(rank, attendance) {
    var answer = 0;
    var map = new Object
    var winner_lst = []
    rank.forEach((ranking,idx)=>{
        map[ranking] = idx
    })
    
    rank.sort((a,b)=>(a-b))
    
    rank.forEach((ranking)=>{
        var student_num = map[ranking]
        if (attendance[student_num]){
            if (winner_lst.length <3){
                winner_lst.push(student_num)
            }
        }
    })
    
    let i = 10000
    winner_lst.forEach((ranking)=>{
        const value = ranking * i
        answer+=value
        i = i/100
    })
    
    console.log(map)
    console.log(winner_lst)
    return answer;
}

/*
일단, 등수를 key, 그 학생 번호(인덱스)를 value로 object에 저장하자
rank를 오름차순으로 정렬
rank를 돌면서, 그 rank의 학생 번호(인덱스)가 attendance의 인덱스로서 true면 ->
result배열에 push
그 다음 처리
*/