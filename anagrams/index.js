// --- Directions
// Check to see if two provided strings are anagrams of eachother.
// One string is an anagram of another if it uses the same characters
// in the same quantity. Only consider characters, not spaces
// or punctuation.  Consider capital letters to be the same as lower case
// --- Examples
//   anagrams('rail safety', 'fairy tales') --> True
//   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
//   anagrams('Hi there', 'Bye there') --> False

function anagrams(stringA, stringB) {
    return cleanString(stringA) === cleanString(stringB);
}

function cleanString(string) {
    return string.replace(/[^\w]/g, '').split('').sort().join("");
}

anagrams("Whoa! Hi!", "Hi! Whoa!");

module.exports = anagrams;



// function anagrams(stringA, stringB) {
//     let anagObj = {};
//     const regex = /!/gi;
//     stringA = stringA.replace(regex, "");
//     stringA = stringA.toLowerCase();
//     stringB = stringB.replace(regex, "");
//     stringB = stringB.toLowerCase();
//     console.log(stringA);

//     for (let element of stringA){
//       if(anagObj[element]==null)  anagObj[element] = 1;
//       else anagObj[element]++;
//     }

//     for (let element of stringB){
//         if(anagObj[element]==null || anagObj[element]< 0 ) return false;
//         anagObj[element]--;
//     }


//     console.log(anagObj);
//     return true;
// }