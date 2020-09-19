// --- Directions
// Given the root node of a tree, return
// an array where each element is the width
// of the tree at each level.
// --- Example
// Given:
//     0
//   / |  \
// 1   2   3
// |       |
// 4       5
// Answer: [1, 3, 2]

function levelWidth(root) {
    const ans = [0];
    const arr = [root, 's'];
    
    while(arr.length > 1){
        const node  = arr.shift();
        if(node === 's'){
            arr.push('s');
            ans.push(0);
        } else {
            arr.push(...node.children);
            ans[ans.length-1]++;
        }
    }


    return ans;
}


module.exports = levelWidth;
