/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
/*======== <Solution 1> ========*/
    let str = Math.abs(x).toString();
    let reversed = "";
    for (let i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }
    if (Number(reversed) > Math.pow(2, 31)) return 0;
    return Number(reversed) * Math.sign(x);
    
/*======== <Solution 2> ========*/
    sign = Math.sign(x);
    x = Math.abs(x);
    let reversed = 0;
    while (x > 0) {
        let num = x % 10;
        x = Math.floor(x / 10);
        reversed = reversed * 10 + num;
    }
    if (reversed > Math.pow(2, 31)) return 0;
    return reversed * sign;
    
/*======== <Solution 3> ========*/
    const reversed = Math.abs(x).toString().split('').reverse().join('');
    if (reversed > Math.pow(2, 31)) return 0;
    return reversed * Math.sign(x);
};
