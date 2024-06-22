function solution(my_string, queries) {
    function swap(lst){
        var half = Math.floor(lst.length/2)
        var tmp ;
        for(let i = 0; i<half; i++){
            tmp = lst[i]
            lst[i] = lst[lst.length-i-1]
            lst[lst.length-i-1] = tmp
            
        }
        return lst
    }
    
    var lst = [...my_string]   
    queries.forEach((element)=>{
        [s,e] = element
        
        var tmp_lst = lst.slice(s,e+1)
        tmp_lst = swap(tmp_lst)
        lst = [...lst.slice(0,s),...tmp_lst,...lst.slice(e+1)]
        
        
    })
    // 배열 lst를 문자열로 변환하여 반환
    var answer = lst.join('');
    return answer;
}

/*
1. for문을 돌면서, index를 뽑아낸다 
2. string을 리스트로 바꾼다
3. swap하는 로직 입힌다
 - swap어떻게해? -> s~e범위의 절반까지 돌기

*/