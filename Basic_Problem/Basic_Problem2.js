const prompt = require("prompt-sync")()
function Deci_face(n) {
    return  `the opposite face of ${n} is  : ${7-n}`
}

let n  = prompt("Enter the face You want : ")

console.log(Deci_face(n));

function Nth_Math(a1 , a2 , n) {
    let d = a2 - a1
    return `the ${n}th term is :  ${a1 + (n - 1) * d}`
}

console.log(Nth_Math(4 , 4 , 10));

function SumDigits(n) {
  let result = 0;
  while (n > 0) {
    result += n % 10;

    n = Math.floor(n / 10);
  }
  return result;
}

console.log(SumDigits(687));

function ReserveDigits(n) {
  let numbers = 0

  while (n > 0) {
    numbers = numbers * 10 + n % 10;

    n = Math.floor(n / 10);
  }
   return  numbers
}

console.log(ReserveDigits(200));


function PrimeNum(n) {
  if (n <= 1) {
     return false
  }

  for (let i = 2; i < n; i++) {
    
    if (n % i == 0) {
        return `No it's not a Prime number `
    }
    
  }

  return `Yes is Prime Number ${true}`
}

console.log(PrimeNum(27));
