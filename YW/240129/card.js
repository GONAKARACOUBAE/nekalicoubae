const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\r\n");

N = Number(input.shift());

const numberList = input.map((number) => Number(number));
const cardDack = numberList.reduce((acc, num) => {
  acc[num] = (acc[num] || 0) + 1;
  return acc;
}, {});

console.log("numberList : ", numberList);
console.log("CardDack : ", cardDack);
const maxCount = Math.max(...Object.values(cardDack));
const maxCountKeys = Object.keys(cardDack).filter(
  (key) => cardDack[key] === maxCount
);
const maxCountMinKey = Math.min(...maxCountKeys.map(Number));

console.log(maxCountMinKey);
