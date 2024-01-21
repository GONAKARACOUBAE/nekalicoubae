const sequence = [1, 2, 3, 4, 5];
const key = 7;

const solution = (sequence, key) => {
  let left = 0;
  let right = 0;
  let sum = sequence[0];
  const result = [];

  while (right < sequence.length) {
    if (sum < key) {
      right++;
      sum += sequence[right];
    } else if (sum > key) {
      sum -= sequence[left];
      left++;
    } else {
      result.push([left, right]);
      right++;
      sum += sequence[right];
    }
  }

  return result.sort(sortFunction)[0];
};

const sortFunction = (a, b) => {
  const lenDiff = Math.abs(a[0] - a[1]) - Math.abs(b[0] - b[1]);
  if (lenDiff !== 0) return lenDiff;
  return a[0] - b[0];
};

const answer = solution(sequence, key);
console.log("정답은 : ", answer + " 입니다.");
