const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const squareLength = Number(input.shift());
let recordLocation = new Array(squareLength).fill(0);
let count = 0;

const canPutQueen = (nowColumn) => {
  for (let column = 0; column < nowColumn; column++) {
    if (
      recordLocation[column] === recordLocation[nowColumn] ||
      Math.abs(recordLocation[nowColumn] - recordLocation[column]) === Math.abs(nowColumn - column)
    ) {
      return false;
    }
  }
  return true;
};

const nQueen = (column) => {
  if (column === squareLength) {
    count += 1;
  } else {
    for (let row = 0; row < squareLength; row++) {
      recordLocation[column] = row;
      if (canPutQueen(column) === true) {
        nQueen(column + 1);
      }
    }
  }
};

nQueen(0);
console.log(count);
