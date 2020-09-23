// Valid Palindrome II
// Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

// Example 1:
// Input: "aba"
// Output: True
// Example 2:
// Input: "abca"
// Output: True
// Explanation: You could delete the character 'c'.
// Note:
// The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

var validPalindrome = function (s) {
  let isVal = isPalindrome(s, 0, s.length - 1);
  if (isVal[0] === false) {
    let left = isVal[1];
    let right = isVal[2];
    isVal = isPalindrome(s, left + 1, right);
    if (isVal[0] === false) {
      isVal = isPalindrome(s, left, right - 1);
    }
  }
  return isVal[0];
};


var isPalindrome = function (s, left, right) {
  s = s.toLowerCase().replace(/[\W_]/g, "");
  while (left < right) {
    if (s[left] !== s[right]) return [false, left, right];
    left++;
    right--;
  }
  return [true];
};