function centuryFromYear(year) {
    var x = (Math.floor((year-1)/100)) + 1;
    return x; 
}

console.log(centuryFromYear(1700)) // 17
console.log(centuryFromYear(1800)) // 18
console.log(centuryFromYear(1)) // 1
console.log(centuryFromYear(1702)) // 18
console.log(centuryFromYear(2000)) // 20
console.log(centuryFromYear(2020)) // 21