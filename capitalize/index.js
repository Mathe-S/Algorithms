// --- Directions
// Write a function that accepts a string.  The function should
// capitalize the first letter of each word in the string then
// return the capitalized string.
// --- Examples
//   capitalize('a short sentence') --> 'A Short Sentence'
//   capitalize('a lazy fox') --> 'A Lazy Fox'
//   capitalize('look, it is working!') --> 'Look, It Is Working!'

function capitalize(str) {
    const separatedSTR = str.split(" ");
    console.log(separatedSTR);

    for(let ind in separatedSTR){
        separatedSTR[ind] = separatedSTR[ind][0].toUpperCase() + separatedSTR[ind].slice(1);
    }

    return separatedSTR.join(' ');
}

capitalize('a short sentence');

module.exports = capitalize;
