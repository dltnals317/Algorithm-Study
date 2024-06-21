function solution(strArr) {
    var answer = 0;
    const StrLength = new Object()
    var l = ' '
    for (let i = 0; i<strArr.length; i++){
        l =strArr[i].length
        if (StrLength[l]){
            StrLength[l] +=1
        }
        else{
            StrLength[l] =1
        }
    }
    cnt_arr = Object.values(StrLength)
    answer = Math.max(...cnt_arr)
    return answer;
}


//1. 배열을 순회하면서,  문자열의 길이를 key로 하는 객체에, value를 1 증가시키기
