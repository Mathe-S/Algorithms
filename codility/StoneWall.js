class Stack {

  constructor() {
    this.data = []
    this.top = 0
  }

  push(element) {
    this.data.push(element)
    this.top++
  }

  pop() {
    if (!this.isEmpty()) {
      this.top--;
      return this.data.pop()
    }
  }

  peek() {
    return this.data[this.top - 1]
  }

  length() {
    return this.top
  }

  search(element) {
    this.data.forEach((e, i) => {
      if (e === element) return i
    })

    return -1
  }

  isEmpty() {
    return this.top === 0
  }

}

function solution(H) {

  let myStack = new Stack()
  myStack.push(H[0])
  let cubics = 0

  for (let i = 1; i < H.length; i++) {

    if (H[i] < H[i - 1]) {
      while (H[i] < myStack.peek()) {
        myStack.pop()
        cubics++
      }

      if (H[i] !== myStack.peek()) myStack.push(H[i])
    } else {
      if (H[i] === H[i - 1]) continue;
      myStack.push(H[i])
    }

  }

  return cubics + myStack.length()
}

let H = []

H[0] = 8
H[1] = 8
H[2] = 5
H[3] = 7
H[4] = 9
H[5] = 8
H[6] = 7
H[7] = 4
H[8] = 8
solution(H)