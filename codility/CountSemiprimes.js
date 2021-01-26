function solution(N, P, Q) {

  let myArr = new Array(N + 1).fill(true)
  let primeObj = []
  let notprimeObj = []


  let i = 2

  while (i * i <= N) {

    let j = i * i

    while (j < N) {
      myArr[j] = false
      j += i
    }

    i++
  }

  for (let i in myArr) {
    if (!myArr[i]) primeObj.push(i)
    else notprimeObj.push(i)

  }

  let len = notprimeObj.length
  let count = 0
  let countArr = new Array(N + 1).fill(0)

  for (let i = 2; i < len; i++) {
    let j = i

    while (j < len && notprimeObj[i] * notprimeObj[j] <= N) {
      countArr[notprimeObj[i] * notprimeObj[j]]++
      j++
    }
  }

  let ansArr = [0]
  for (let i = 1; i <= N; i++) {
    ansArr[i] = ansArr[i - 1] + countArr[i]
  }

  let myAns = []
  for (let i in P) {
    myAns.push(ansArr[Q[i]] - ansArr[P[i] - 1])
  }

  return myAns
}



let P = [], Q = [], N = 26

P[0] = 1
P[1] = 4
P[2] = 16

Q[0] = 26
Q[1] = 10
Q[2] = 20

solution(N, P, Q)

