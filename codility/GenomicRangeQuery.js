function solution(S, P, Q) {

  const worthObj = {
    "A": 1,
    "C": 2,
    "G": 3,
    "T": 4,
  }

  const worthArr = {}
  const ansArr = []
  let distanceObj = {
    "1": null,
    "2": null,
    "3": null,
    "4": null
  }

  S.split("").forEach((element, index) => {

    if (worthArr[index - 1]) {
      if (distanceObj["1"] !== null) distanceObj["1"]++
      if (distanceObj["2"] !== null) distanceObj["2"]++
      if (distanceObj["3"] !== null) distanceObj["3"]++
      if (distanceObj["4"] !== null) distanceObj["4"]++
    }

    distanceObj[worthObj[element]] = 0
    worthArr[index] = {
      ...distanceObj
    }

  });

  // console.log('worthArr: ', worthArr);

  Q.forEach((element, index) => {
    const distance = element - P[index]

    if ((worthArr[element]["1"] !== null) && (worthArr[element]["1"] <= distance)) ansArr.push(1)
    else if ((worthArr[element]["2"] !== null) && (worthArr[element]["2"] <= distance)) ansArr.push(2)
    else if ((worthArr[element]["3"] !== null) && (worthArr[element]["3"] <= distance)) ansArr.push(3)
    else if ((worthArr[element]["4"] !== null) && (worthArr[element]["4"] <= distance)) ansArr.push(4)

  })

  return ansArr
}



solution("C", [0], [0])
