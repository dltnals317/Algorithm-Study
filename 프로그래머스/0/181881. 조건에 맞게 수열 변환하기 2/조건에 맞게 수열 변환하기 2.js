function solution(arr) {
    function transfer_arr(lst) {
        return lst.map(element => {
            if (element >= 50 && element % 2 === 0) {
                return element / 2;
            } else if (element < 50 && element % 2 !== 0) {
                return 2 * element + 1;
            } else {
                return element; // 변환할 필요가 없는 경우
            }
        });
    }
    
    var answer = 0;
    let arr_copy = [...arr] //배열을 복사
    while (true){
         let new_arr = transfer_arr(arr_copy)
         if (JSON.stringify(arr_copy) === JSON.stringify(new_arr)) {
            return answer;
        }
        
        else
        {
            answer+=1
            arr_copy = [...new_arr];
        }
    }

    return answer;
}


/*
<문제 이해>
배열을 탐색하면서 조건에 따라 값을 바꾼다.
그렇게 새로 완성된 배열에 대해 , 이전 배열과 결과가 같은지 확인하는 로직을 추가한다.
-> 변함이 없다면 cnt출력

*/