const fs = require("fs");
// const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

// const input = fs.readFileSync("/dev/stdin").toString().split("\n").slice(0, -1);
// const NM = input[0].split(" ");
// const [n, m] = NM.map((el) => Number(el));

const n = 4;
const m = 4;
let answer = "";
let selected = [];
let a = "";
const solution = (number) => {
  if (number === m) {
    answer += `${selected.join(" ")}\n`;
    return;
  } else {
    for (let cand = 1; cand <= n; cand++) {
      if (!selected.includes(cand)) {
        selected[number] = cand;
        solution(number + 1);
        selected[number] = 0;
      }
    }
  }
};

solution(0);
console.log(answer);
