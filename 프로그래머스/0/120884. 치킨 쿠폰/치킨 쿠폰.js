function solution(chicken) {
    var answer = 0;
    var cupon= chicken;
    var service = 0;
    for(cupon = chicken; cupon>0; cupon=cupon-10){
        if (cupon>=10){
            service +=1
            cupon+=1
        }
        
    }
    answer = service
    return answer;
}



/*
1. chicken을 거꾸로 for문 돌면서, 10씩 빼고, cupon+=1,(10이 안빼지면 멈추기)
2. cupon을 10씩 빼면서, service에 1씩 추가 & cupon에 1 추가
*/