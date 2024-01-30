const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

N = Number(input.shift());

const numberList = input[0].split(" ").map(Number);
const sortedList = input[0]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

const P = new Array(N).fill(false);

numberList.forEach((number, index) => {
  P[index] = sortedList.findIndex((sortNumber, sortIndex) => {
    if (sortNumber === number && !P.includes(sortIndex)) return true;
  });
});

console.log(P.join(" "));
