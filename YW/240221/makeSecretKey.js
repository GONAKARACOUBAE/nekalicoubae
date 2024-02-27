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

const wordSortedList = input.shift().split(" ").sort();

const countVowel = (wordLists) => {
  const moList = ["a", "e", "i", "o", "u"];
  const result = [];
  wordLists.map((wordList) => {
    let moCount = 0;
    let jaCount = 0;
    wordList.map((word) => {
      if (moList.includes(word)) {
        moCount += 1;
      } else {
        jaCount += 1;
      }
    });
    if (jaCount >= 2 && moCount >= 1) {
      result.push(wordList.join("") + "\n");
    }
  });
  return result;
};

const getCombination = (arr, selectNumber) => {
  if (selectNumber === 1) {
    return arr.map((element) => [element]);
  }
  const results = [];
  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombination(rest, selectNumber - 1);
    const attached = combinations.map((combination) => [fixed, ...combination]);
    results.push(...attached);
  });
  return results;
};

const combinationList = getCombination(wordSortedList, keyLength);
const answerList = countVowel(combinationList);
answerList.map((answerKey) => {
  answer += answerKey;
});
console.log(answer.trim());
