const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

input.shift();

let answer = "";

const students = input.map((el) =>
  el.split(" ").map((v, i) => {
    return i === 0 ? v : Number(v);
  })
);

students.sort((a, b) => {
  return b[1] - a[1] || a[2] - b[2] || b[3] - a[3] || (a[0] > b[0] ? 1 : -1);
});

students.map((el) => (answer += el[0] + "\n"));

console.log(answer);
