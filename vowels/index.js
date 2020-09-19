function isBeautifulString(inputString) {
  const string = inputString.split("");
  const ansObj = {};

  string.map(char => {
    if (ansObj[char.charCodeAt()] > 0) ansObj[char.charCodeAt()]++;
    else ansObj[char.charCodeAt()] = 1;
  });

  let sortedObject = [];

  for (let key in ansObj) {
    sortedObject.push([parseInt(key), ansObj[key]]);
  }

  sortedObject.sort((a, b) => a[0] > b[0]);

  console.log(sortedObject[0][0]);

  for (let i = 0; i < sortedObject.length - 1; i++) {
    if (sortedObject[i][1] > sortedObject[i + 1][1]) {
      return false;
    }
  }

  return true;
}


isBeautifulString("bbc");