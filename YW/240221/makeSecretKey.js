const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");
const [keyLength, wordNumber] = input
  .shift()
  .split(" ")
  .map((number) => Number(number));
let answer = "";

const wordList = input.shift().split(" ").sort();

const countVowel = (wordList) => {
  let moCount = 0;
  let jaCount = 0;
  wordList.map((word) => {
    if (word === "a" || word === "e" || word === "i" || word === "o" || word === "u") {
      moCount += 1;
    } else {
      jaCount += 1;
    }
  });
  if (jaCount >= 2 && moCount >= 1) {
    return true;
  } else {
    return false;
  }
};

const makeSecretKey = (location, secretWordList) => {
  if (location === keyLength) {
    if (countVowel(secretWordList)) {
      answer += secretWordList.join("");
      answer += "\n";
    }
  }
  console.log("location : ", location, "secretWordList : ", secretWordList);
  if (keyLength === wordNumber - location && secretWordList.length === keyLength) {
    return;
  }
  secretWordList.push(wordList[location]);
  makeSecretKey(location + 1, secretWordList);
  secretWordList.pop();
  makeSecretKey(location + 1, secretWordList);
};
makeSecretKey(0, []);
console.log(answer);
