const fs = require("fs");
// const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync("/dev/stdin").toString().split("\n").slice(0, -1);
const NM = input[0].split(" ");
const [max_number, line] = NM.map((el) => Number(el));

const visited = new Array(max_number);
const output = [];
let result = "";

function dfs(idx, cnt) {
  if (cnt === line) {
    result += `${output.join(" ")}\n`;
    return;
  }

  for (let i = idx; i < max_number; i++) {
    if (visited[i] === true) continue;
    visited[i] = true;
    output.push(i + 1);
    dfs(i, cnt + 1);
    output.pop();
    visited[i] = false;
  }
}

dfs(0, 0);
console.log(result);
