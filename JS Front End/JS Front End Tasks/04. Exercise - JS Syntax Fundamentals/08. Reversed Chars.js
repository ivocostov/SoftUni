function reversedChars(param_1, param_2, param_3) {
    let newString = (`${param_1}`+`${param_2}`+`${param_3}`).split("")
    let reversedString = newString.reverse().join(' ')

    console.log(reversedString)
}

reversedChars('A','B','C')
reversedChars('1','L','&')