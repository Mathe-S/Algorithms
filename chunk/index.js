// --- Directions
// Given an array and chunk size, divide the array into many subarrays
// where each subarray is of length size
// --- Examples
// chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
// chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
// chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
// chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
// chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

function chunk(array, size) {
    const chunked = [];

    for(let element of array){
        const last = chunked[chunked.length-1];

        if(!last || last.length==size){
            chunked.push([element]);
        } else {
            last.push(element);
        }
    }
    return chunked;
}

chunk([1, 2, 3, 4, 5], 2);

module.exports = chunk;


// function chunk(array, size) {
//     let ansArr = [];
//     let exArr = [];

//     for (let i in array){
//         exArr.push(array[i]);
//         // console.log(exArr);
//         if(exArr.length === size) {
//             ansArr.push(exArr);
//             exArr=[];
//         }
//     }
//     if (exArr.length) ansArr.push(exArr);
//     // console.log(ansArr);
//     return ansArr;
// }



// function chunk(array, size) {
//     const ansArr = [];
//     let index = 0;

//     while (index < array.length){
//         ansArr.push(array.slice(index, index+size));
//         index+=size;
//     }

//     return ansArr;

// }