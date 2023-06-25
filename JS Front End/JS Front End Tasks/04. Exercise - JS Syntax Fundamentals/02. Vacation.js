// function vacation(group_of_people, type_of_group, day_of_the_week) {
//     let total_price = 0
//     if (type_of_group === 'Students') {
//         if (day_of_the_week === 'Friday') {
//             let price_per_day = 8.45
//             total_price = group_of_people * price_per_day
//         } else if (day_of_the_week === 'Saturday') {
//             let price_per_day = 9.8
//             total_price = group_of_people * price_per_day
//         } else if (day_of_the_week === 'Sunday') {
//             let price_per_day = 10.46
//             total_price = group_of_people * price_per_day
//         }
//         if (group_of_people >= 30){
//                 total_price -= total_price * 0.15
//         }
//
//     } else if (type_of_group === 'Business') {
//         if (day_of_the_week === 'Friday') {
//             let price_per_day = 10.9
//             total_price = group_of_people * price_per_day
//
//             if (group_of_people >= 100) {
//                 total_price -= total_price * 10
//             }
//         } else if (day_of_the_week === 'Saturday') {
//             let price_per_day = 15.6
//             total_price = group_of_people * price_per_day
//
//             if (group_of_people >= 100) {
//                 total_price -= total_price * 10
//             }
//
//         } else if (day_of_the_week === 'Sunday') {
//             let price_per_day = 16
//             total_price = group_of_people * price_per_day
//             if (group_of_people >= 100) {
//                 total_price -= total_price * 10
//             }
//         }
//
//     } else if (type_of_group === 'Regular') {
//         if (day_of_the_week === 'Friday') {
//             let price_per_day = 15
//             total_price = group_of_people * price_per_day
//
//             if (group_of_people >= 10 && group_of_people <= 20) {
//             total_price -= total_price * 0.05
//             }
//         } else if (day_of_the_week === 'Saturday') {
//             let price_per_day = 20
//             total_price = group_of_people * price_per_day
//
//             if (group_of_people >= 10 && group_of_people <= 20) {
//             total_price -= total_price * 0.05
//             }
//         } else if (day_of_the_week === 'Sunday') {
//             let price_per_day = 22.5
//             total_price = group_of_people * price_per_day
//
//             if (group_of_people >= 10 && group_of_people <= 20) {
//             total_price -= total_price * 0.05
//             }
//         }
//
//     }
//
//     console.log(`Total price: ${total_price.toFixed(2)}`)
// }


function vacation(group_of_people, type_of_group, day_of_the_week) {

    let price_list = {
        'Students': {'Friday': 8.45, 'Saturday': 9.8, 'Sunday': 10.46},
        'Business': {'Friday': 10.9, 'Saturday': 15.6, 'Sunday': 16},
        'Regular': {'Friday': 15, 'Saturday': 20, 'Sunday': 22.5}
    }
    let total_price = price_list[type_of_group][day_of_the_week] * group_of_people

    if (type_of_group === 'Students' ) {
        if (group_of_people >= 30) {
            total_price -= total_price * 0.15
        }
    } else if (type_of_group === 'Business') {
        if (group_of_people >= 100) {
            total_price -= 10 * price_list[type_of_group][day_of_the_week]
        }
    } else if (type_of_group === 'Regular') {
        if (group_of_people >= 10 && group_of_people <= 20) {
            total_price -= total_price * 0.05
        }
    }

    console.log(`Total price: ${total_price.toFixed(2)}`)
}


vacation(30,"Students","Sunday")
vacation(40,"Regular","Saturday")