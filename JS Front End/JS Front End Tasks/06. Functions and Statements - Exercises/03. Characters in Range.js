function charctersInRange(char_1, char_2) {
    let charOneAsciiCode = char_1.charCodeAt(0)
    let charTwoAsciiCode = char_2.charCodeAt(0)
    charsArray = []

    if (charOneAsciiCode < charTwoAsciiCode) {
        for (let i = charOneAsciiCode + 1; i < charTwoAsciiCode; i++) {
            charsArray.push(String.fromCharCode(i))
        } 
    } else {
        for (let i = charTwoAsciiCode + 1; i < charOneAsciiCode; i++) {
            // console.log(String.fromCharCode(i))
            charsArray.push(String.fromCharCode(i))
        }
    }
    console.log(charsArray.join(' '))
}

charctersInRange('a', 'd')
charctersInRange('#', ':')
charctersInRange('C', '#')
