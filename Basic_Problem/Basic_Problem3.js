// function PowerCheck(x, y) {
//   if (x === 1) {
//     return y === 1;
//   }

//   // Repeatedly compute power of x
//   let pow = 1;

//   while (pow < y) {
//     pow *= x;
//   }
//   // Check if power of x becomes y
//   return pow === y;
// }

// console.log(PowerCheck(3, 9))

// function distance_Points(x1, y1, x2, y2) {
//   let Distance = 0;

//   Distance = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
//   Dis = Math.round(Distance * 100)/100;
//   return Dis;
// }

// console.log(distance_Points(3, 4, 4, 3));

// function Check_triangle(a, b, c) {
//   if ((a + b > c) && (a + c > b) && (b + c > a)) {
//     return "Valid Triangle ✅"
//   } else {
//     return "inValid Triangle ❌";
//   }
// }

// console.log(Check_triangle(7, 10, 5));

class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

// Returns true if two rectangles (l1, r1) and (l2, r2) overlap
function doOverlap(l1, r1, l2, r2) {
    // If one rectangle is to the left of the other
    if (l1.x > r2.x || l2.x > r1.x)
        return false;

    // If one rectangle is above the other
    if (r1.y > l2.y || r2.y > l1.y)
        return false;

    return true;
}

// Driver code
const l1 = new Point(0, 10);
const r1 = new Point(10, 0);
const l2 = new Point(5, 5);
const r2 = new Point(15, 0);

if (doOverlap(l1, r1, l2, r2)) {
    console.log("Rectangles Overlap");
} else {
    console.log("Rectangles Don't Overlap");
}

let x = "shucayb" 
console.log(x)