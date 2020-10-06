var canWinNim = function (n) {
  return n % 4 != 0;
};

var hammingDistance = function (x, y) {
  return ((x ^ y).toString(2).match(/1/g) || []).length;
};
