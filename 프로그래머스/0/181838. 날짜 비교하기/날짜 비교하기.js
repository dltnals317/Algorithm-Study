function solution(date1, date2) {
    var answer = 0;
    [year1,month1,day1] = date1;
    [year2,month2,day2] = date2;
    
    if (year1 < year2)
    {
        return 1;
    }
    else if(year1 === year2)
    {
        if (month1 < month2)
        {
            return 1;
        }
        else if (month1 === month2)
        {
            if (day1 < day2){
            return 1;
        }
        else
        {
            return 0;
        }    
        }
    }
    else
    {
        return 0;
    }
    return answer;
}

//1. if-else를 년->월->일을 비교기준으로 잘 쓰면 될듯
//2. 배열의 구조분해할당 활용해보자