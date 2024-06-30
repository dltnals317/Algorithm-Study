function solution(my_string, overwrite_string, s) {
    var answer = '';
    var my_string_lst = [...my_string]
    
    
    for(let i=0; i<overwrite_string.length; i++){
        my_string_lst[i+s] = overwrite_string[i]
    }
    
    
    console.log("my_string_lst",my_string_lst)
    
    answer = my_string_lst.join('')
    return answer;
}



/*
문자열 슬라이싱
s ~ s+overwrite_string.length 만큼에 해당하는 부분을 기준으로, 문자열 슬라이싱


*/