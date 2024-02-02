const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map(Number));

const requireNumber = input[0][1];
const numberList = input[1];
let answer = 0;
let sumNumber = 0;

const dfs = (location, sumNumber) => {
  if (location === numberList.length) {
    return;
  }
  sumNumber += numberList[location];

  if (isSameRequireNumber(sumNumber)) {
    answer += 1; // 문자열로 변환하여 추가
  }
  dfs(location + 1, sumNumber);
  dfs(location + 1, sumNumber - numberList[location]);
};

const isSameRequireNumber = (nowNumber) => {
  return requireNumber === nowNumber;
};

dfs(0, sumNumber);
console.log(answer);
