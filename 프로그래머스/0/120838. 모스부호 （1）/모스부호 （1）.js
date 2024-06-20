function solution(letter) {
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    
    var answer = '';
    const tmp = ''
    lst = letter.split(" ")
    for (let i = 0; i < lst.length; i++){
        lst[i] = morse[lst[i]]
    }
    answer = lst.join("")
    return answer;
}


//1. 공백을 기준으로 문자열을 나눠서, 배열로 만든다 by split문법
//2. 배열의 원소를 문자열로 합친다