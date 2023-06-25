function theatrePromotions(day_type, age) {
    if (age <= 0 || age > 122) {
        console.log('Error!')
    } else {
        if (day_type === 'Weekday') {
            if (age >= 0 && age <= 18) {
                let ticket_prise = 12
                console.log(`${ticket_prise}$`)
            } else if (age > 18 && age <= 64) {
                let ticket_prise = 18
                console.log(`${ticket_prise}$`)
            } else if (age > 64 && age <= 122) {
                let ticket_prise = 12
                console.log(`${ticket_prise}$`)
            }

        } else if (day_type === 'Weekend') {
            if (age >= 0 && age <= 18) {
                let ticket_prise = 15
                console.log(`${ticket_prise}$`)
            } else if (age > 18 && age <= 64) {
                let ticket_prise = 20
                console.log(`${ticket_prise}$`)
            } else if (age > 64 && age <= 122) {
                let ticket_prise = 15
                console.log(`${ticket_prise}$`)
            }

        } else if (day_type === 'Holiday') {
            if (age >= 0 && age <= 18) {
                let ticket_prise = 5
                console.log(`${ticket_prise}$`)
            } else if (age > 18 && age <= 64) {
                let ticket_prise = 12
                console.log(`${ticket_prise}$`)
            } else if (age > 64 && age <= 122) {
                let ticket_prise = 10
                console.log(`${ticket_prise}$`)
            }
        }
    }
}

theatrePromotions('Weekday',42)
theatrePromotions('Holiday', -12)
theatrePromotions('Holiday', 15)
