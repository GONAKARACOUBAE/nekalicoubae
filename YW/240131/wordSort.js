const fs = require("fs");
const [, ...wordList] = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const setWord = new Set(wordList);

const uniqueWord = Array.from(setWord);

const sortedWord = uniqueWord.sort((a, b) => {
  if (a.length < b.length) {
    return -1;
  } else if (a.length === b.length) {
    if (a < b) {
      return -1;
    } else return 1;
  }
});

sortedWord.map((word) => console.log(word));
