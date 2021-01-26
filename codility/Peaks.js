function solution(A) {

  let len = A.length
  let peaks = new Array(len).fill(false)
  let nextPeak = new Array(len)
  let lastPeak = -1
  let peakCount = 0

  for (let i = 1; i < len - 1; i++) {
    if (A[i] > A[i - 1] && A[i] > A[i + 1]) {
      peaks[i] = true
      lastPeak = i
    }
  }

  for (let i = len - 1; i >= 0; i--) {
    if (peaks[i]) {
      lastPeak = i
      peakCount++
    }
    nextPeak[i] = lastPeak
  }

  if (lastPeak === -1) return 0

  let i = 2
  let divisions = 1

  while (i <= peakCount) {
    let flag = true
    let step = len / i

    if (len % i === 0) {
      let j = i + 1
      while (j < len) {
        let currpeak = nextPeak[j]
        if (currpeak === nextPeak[j + step] && currpeak > j + step) {
          flag = false
          break
        }
        j += step
      }

      if (flag) divisions = i
    }
    i++
  }

  return divisions
}

solution([1, 3, 2, 1])
