function factorialDivision(num_1, num_2) {
    let firstFactorialNumberResult = 1
    let secondFactorialNumberResult = 1

    for (let fFN = 1; fFN <= num_1; fFN++) {
        firstFactorialNumberResult *= fFN
    }

    for (let sFN = 1; sFN <= num_2; sFN++) {
        secondFactorialNumberResult *= sFN
    }

    let result = firstFactorialNumberResult / secondFactorialNumberResult
    console.log(result.toFixed(2))
}

// **************************************************************************************************


// function calculateFactorial(num) {
//     let sum = 1;
  
//     for (let index = 1; index <= num; index++) {
//       sum *= index;
//     }
  
//     return sum;
//   }
  
//   function solve(x, y) {
//     return (calculateFactorial(x) / calculateFactorial(y)).toFixed(2);
//   }

factorialDivision(5, 2)
factorialDivision(6, 2)