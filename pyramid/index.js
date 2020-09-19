// --- Directions
// Write a function that accepts a positive number N.
// The function should console log a pyramid shape
// with N levels using the # character.  Make sure the
// pyramid has spaces on both the left *and* right hand sides
// --- Examples
//   pyramid(1)
//       '#'
//   pyramid(2)
//       ' # '
//       '###'
//   pyramid(3)
//       '  #  '
//       ' ### '
//       '#####'

function pyramid(n, row = 0, level = '') {
    if(n === row) return;
    const length = (n*2)-1;
    const middle = Math.floor(length/2);


    if(level.length === length){
        console.log(level);
        return pyramid(n, row+1);
    }

    if(level.length>=(middle-row) && level.length<=(middle+row)) level+='#';
    else level+='b'; 
    pyramid(n, row, level);

}

pyramid(3);

module.exports = pyramid;


// function pyramid(n) {
//     const length = (n*2)-1;
//     const middle = Math.floor(length/2);
  
//     for(let i=0; i<n; i++){
//         let level = '';

//         for(let j=0; j<length; j++){
//             if(j>=(middle-i) && j<=(middle+i)) level+='#';
//             else level+='b'; 
//             // console.log(i);
//             // console.log(j);
//             // console.log(level);
//             // console.log(length);
//         }
//         console.log(level);
//     }

//     return;
// }