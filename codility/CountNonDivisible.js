function solution(A) {

  let len = A.length
  let max = Math.max(...A)
  let eraObj = {}
  let ansObj = {}
  A.forEach((element, i) => {
    eraObj[element] = eraObj[element] ? eraObj[element] + 1 : 1
    ansObj[element] = len
  });

  for (let i of Object.keys(eraObj)) {
    let num = eraObj[i]
    let j = parseInt(i)

    while (j <= max) {
      if (eraObj[j]) {
        if (j % i === 0) {
          if (j == i) ansObj[j] -= eraObj[j]
          else ansObj[j] -= num
        }
      }
      j += parseInt(i)
    }

  }

  const ansArr = []

  for (let e of A) ansArr.push(ansObj[e])

  return ansArr
}

let A = []
A[0] = 3
A[1] = 1
A[2] = 2
A[3] = 3
A[4] = 6
solution(A)