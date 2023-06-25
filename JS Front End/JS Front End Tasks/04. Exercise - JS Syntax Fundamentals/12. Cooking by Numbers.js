"use strict";

function cookingByNumbers(
    // number, operation_1, operation_2, operation_3, operation_4, operation_5
    number, ...args
    ) {
        
        let current_number = Number(number)
        
        function mathOperations(arg) {
            
            let availableOperations = {
            'chop': current_number / 2,
            'dice': Math.sqrt(current_number),
            'spice': current_number + 1,
            'bake': current_number * 3,
            'fillet': current_number -= current_number * 0.2
            }

            current_number = availableOperations[arg]
            return current_number
        }

        for (let i = 0; i < args.length; i++) {
            current_number = mathOperations(args[i]);
            console.log(current_number)
        }

}

cookingByNumbers('32', 'chop', 'chop', 'chop', 'chop', 'chop')
cookingByNumbers('9', 'dice', 'spice', 'chop', 'bake', 'fillet')
