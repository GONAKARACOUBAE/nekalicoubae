// 오늘의 문제 풀이 1번
const solution = (arr) => {
  let answer = [];
  arr.map((number, index) => {
    if (answer[answer.length - 1] !== number) {
      answer.push(number);
    }
  });

  return answer;
};
