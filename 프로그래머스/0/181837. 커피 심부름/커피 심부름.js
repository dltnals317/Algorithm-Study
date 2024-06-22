function solution(order) {
    order_lst = new Object()
    order_lst['americano'] = 0
    order_lst['cafelatte'] = 0
    order.forEach((element)=>{
        if (element.includes('ice')){
            var sp = element.split('ice')
            sp.forEach((coffee)=>{
                if (coffee !== ''){
                    order_lst[coffee]+=1
                }
            })
        }
        else if (element.includes('hot')){
            var sp = element.split('hot')
            sp.forEach((coffee)=>{
                if (coffee !== ''){
                    order_lst[coffee]+=1
                }
            })
            
        }
        else if (element === 'anything'){
            console.log(element)
            order_lst['americano'] +=1
        }
        
        else{
            order_lst[element]+=1
        }
    })
    console.log(order_lst)
    var answer = 0;
    
    for (const [key, value] of Object.entries(order_lst)) {
        if (key === 'americano'){
            answer+=4500*(value)
        }
        else{
            answer+=5000*(value)
        }
}
    return answer;
}


/*
1. includes함수를 사용하여, ice나 hot이 있는지 확인한다.
2. 존재한다면 -> 그걸 기준으로 문자열을 split해서 배열로 만든다
3. 적절한 조건을 적용한다

*/