function solution(my_string) {
    var answer = 0;
    arr = my_string.split(' ')
    tmp = parseInt(arr[0])
    arr.forEach((element,index)=>{
        if (element ==="+"){
            tmp +=parseInt(arr[index+1])
        }
        else if (element ==="-"){
            tmp -=parseInt(arr[index+1])
        }
        
    })
    answer = tmp
    return answer;
}

//연산자가 여러개 올 수가 있음
/*
string을 다루기 쉽게 배열로 바꾼다
forEach문을 돌면서, 연산자가 나오면, 그 위에 값을 연산자에 처리한다

*/
