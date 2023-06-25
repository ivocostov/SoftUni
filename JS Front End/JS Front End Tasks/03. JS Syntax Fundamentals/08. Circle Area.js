function circleArea(argument) {
    let type_of_argument = typeof (argument)
    if (type_of_argument !== 'number') {
        console.log(`We can not calculate the circle area, because we receive a ${type_of_argument}.`)
    } else {
        let circle_area = Math.pow(argument, 2) * Math.PI
        console.log(circle_area.toFixed(2))
    }
}

circleArea(5)
circleArea('name')