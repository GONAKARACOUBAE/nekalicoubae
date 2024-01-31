const fs = require("fs");
const [, ...wordList] = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\r\n");

let extensionList = [];

wordList.map((extension) => {
  extensionList.push(extension.split(".")[1]);
});

const extensionDic = extensionList.reduce((acc, extension) => {
  acc[extension] = (acc[extension] || 0) + 1;
  return acc;
}, {});

const sortedKey = Object.keys(extensionDic).sort();

const sortExtensionDic = sortedKey.reduce((newObj, key) => {
  newObj[key] = extensionDic[key];
  return newObj;
}, {});

Object.keys(sortExtensionDic).map((extension, index) => {
  console.log(extension, sortExtensionDic[extension]);
});
