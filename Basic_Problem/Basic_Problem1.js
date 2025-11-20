function check_N(n) {
    if (n % 2 == 0) {
        return true
    } else {
        return false
    }
}

console.log(check_N(9));

function table_Mult(n) {
    let result = ""
    for (let i = 1; i <= 10; i++) {
        
         result+= `${n} * ${i} = ${n*i}`+ '\n'
        
    }

  return result
}

console.log(table_Mult(5));

function SumNatural_num(n) {
    let result = 0
    for (let i = 1; i <= n; i++) {
         
        result += i**2   
        
    }

    return result
}

console.log(SumNatural_num(8));


function Closest_Num(n , m) {
           
    let closest  = 0
    let minDifference  = Infinity

    for (let i = n-Math.abs(m); i <=n+Math.abs(m); i++) {
        if (i % m == 0) {
            let difference = Math.abs(n-i)

            if (difference < minDifference) {
                closest = i
                minDifference  = difference
            }
        }
        
    }

    return [closest , minDifference]
}



console.log(Closest_Num(20 , 4));
