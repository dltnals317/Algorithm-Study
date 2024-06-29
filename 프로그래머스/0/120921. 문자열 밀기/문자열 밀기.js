function solution(A, B) {
    var location = []
    var location_obj = new Object
    for(let i = 0; i<A.length; i++){
        location[i] = A[i]
    }
    
    var str = ""
    var cnt = 0
    for (let i = 0; i<A.length; i++){
        cnt+=1
        console.log("location",location)
        var changed = Array.from({length:A.length})
        location.forEach((char,idx)=>{
        new_idx = (idx+1)%location.length
        changed[new_idx] = char
    })
        console.log("changed",changed)
        str = changed.join('')
        console.log(str)
        if (str===B){
            return cnt%B.length
        }
        else{
            location = changed
        }
    }
    
    return -1;
}



/*

for문을 돌면서 한칸씩 밀어본다.
문자열의 길이가 5일 때, 5를 벗어나는 지점은 다시 0부터 세야함-> 나머지 연산 이용
how?
-한 칸씩 밀었을 때, 위치 % 문자열 길이를, 해당 char의 위치로 두고 문자를 조정해본 후, B와 비교
- 문자열 길이만큼 위 행위를 반복해도, 바뀌는게 없다면, return -1
*/


/*

for문을 돌면서 한칸씩 밀어본다.
문자열의 길이가 5일 때, 5를 벗어나는 지점은 다시 0부터 세야함-> 나머지 연산 이용
how?
-한 칸씩 밀었을 때, 위치 % 문자열 길이를, 해당 char의 위치로 두고 문자를 조정해본 후, B와 비교
- 문자열 길이만큼 위 행위를 반복해도, 바뀌는게 없다면, return -1
*/