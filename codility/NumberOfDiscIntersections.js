function solution(A) {

  let len = A.length
  let openDisks = 0
  let starPos = []
  let endPos = []
  let ans = 0


  A.forEach((element, i) => {
    starPos.push(i - element)
    endPos.push(i + element)
  });

  starPos.sort((a, b) => a - b)
  console.log('starPos: ', starPos);

  endPos.sort((a, b) => a - b)
  console.log('end: ', endPos);

  let j = 0
  for (let i = 0; i < len; i++) {
    if (starPos[i] <= endPos[j]) {
      ans += openDisks
      openDisks++
    } else {
      j++
      openDisks--
      i--
    }
    // console.log('openDisks: ', openDisks);
  }

  if (ans > 10000000) return -1
  else return ans
};

let A = []
A[0] = 1
A[1] = 5
A[2] = 2
A[3] = 1
A[4] = 4
A[5] = 0


solution(A)