function solution(n, slicer, num_list) {
    var answer = [];
    [a,b,c]=slicer
    if (n===1){
        answer = num_list.slice(0,b+1)
        
    }
    else if (n===2){
        answer = num_list.slice(a)
    }
    
    else if (n===3){
        console.log("a",a)
        console.log("b",b)
        answer = num_list.slice(a,b+1)
    }
    else if (n===4){
        num_list = num_list.slice(a,b+1)
        answer = []
        let step = c
        num_list.forEach((element,index)=>{
            if (index % step === 0){
                answer.push(element)
            }
        })
    }
    return answer;
}


//1. 조건문을 통해 n=1,2,3,4각각을 케이스분류 한다