// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"

function maxChar(str) {
    const obj = {};
    let maxCount = 0;
    let ans = '';

    for(let c in str) {
        obj[str[c]]= (obj[str[c]]+1) || 1;
        if(obj[str[c]] > maxCount) { 
            maxCount=obj[str[c]];
            ans = str[c];
        }
    }


    console.log(obj);
    console.log(maxCount);
    return ans;
}

maxChar("abcccccccd");
module.exports = maxChar;
