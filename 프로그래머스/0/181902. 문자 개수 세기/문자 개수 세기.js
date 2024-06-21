// 소문자 출력
Array.from({ length: 26 }, (v, i) => String.fromCharCode(i + 97));
Array(26).fill().map((v, i) => String.fromCharCode(i + 97));
 
const large_arr = Array.from({ length: 26 }, (v, i) => String.fromCharCode(i + 65));
const small_arr = Array(26).fill().map((v, i) => String.fromCharCode(i + 97));

//spread문법으로 두 배열 합치기
const arr = [
  ...large_arr,
  ...small_arr
];

// 대문자 출력

function solution(my_string) {
    var answer = [];
    const alphavet = new Object()
    arr.forEach((element)=>{alphavet[element] = 0})
    
    for(let i=0; i<my_string.length; i++)
        {
            chr = my_string[i]
            alphavet[chr]+=1
        }
    answer = Object.values(alphavet)
    
    
    return answer;
}


/*
-string을 돌면서, 해당 값이 object의 키값에 존재하는지 확인
-존재한다면, 해당 값을 key로하는 object의 value에 1더함

*/