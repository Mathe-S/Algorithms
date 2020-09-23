// Expression Add Operators
// Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

// Example 1:

// Input: num = "123", target = 6
// Output: ["1+2+3", "1*2*3"] 
// Example 2:

// Input: num = "232", target = 8
// Output: ["2*3+2", "2+3*2"]
// Example 3:

// Input: num = "105", target = 5
// Output: ["1*0+5","10-5"]
// Example 4:

// Input: num = "00", target = 0
// Output: ["0+0", "0-0", "0*0"]
// Example 5:

// Input: num = "3456237490", target = 9191
// Output: []


// Constraints:

// 0 <= num.length <= 10
// num only contain digits.



var addOperators = function (num, target) {
  if (!num || !num.length) return [];

  const ans = [];
  const recurse = (index, prev, curr, val, ops) => {
    if (index === num.length) {
      if (val === target && curr === 0) {
        ans.push(ops.slice(1).join(''));
      }
      return;
    }

    curr = curr * 10 + parseInt(num[index]);
    if (curr > 0) {
      recurse(index + 1, prev, curr, val, ops);
    }

    ops.push('+');
    ops.push(curr.toString());
    recurse(index + 1, curr, 0, val + curr, ops);
    ops.pop();
    ops.pop();

    if (ops.length) {
      ops.push('-');
      ops.push(curr.toString());
      recurse(index + 1, -curr, 0, val - curr, ops);
      ops.pop();
      ops.pop();

      ops.push('*');
      ops.push(curr.toString());
      recurse(index + 1, (curr * prev), 0, val - prev + (curr * prev), ops);
      ops.pop();
      ops.pop();

    }
  };

  recurse(0, 0, 0, 0, []);
  return ans;
}

addOperators('232', 8);