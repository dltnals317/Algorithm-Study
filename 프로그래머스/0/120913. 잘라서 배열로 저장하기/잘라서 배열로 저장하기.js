function solution(my_str, n) {
    var answer = [];
    let i = 0
    while(i<my_str.length){
        sub_str = my_str.slice(i,i+n)
        console.log("sub_str",sub_str)
        answer.push(sub_str)
        i+=n
    }
   
    return answer;
}


/*
i = 0
lst[i:i+6]

i = 6
lst[i:i+6]

*/