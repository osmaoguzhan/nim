const nimValues = new Map();
const MAX_NUMBER = 50000;

const main = () => {
  for (let i = 0; i < MAX_NUMBER; i++) {
    nimValues.set(i, mex(apply127Rule(i)));
  }
  console.log("====================================");
  console.log("Nim Values: ", nimValues);
  console.log("====================================");
};

const apply127Rule = (number) => {
  if (number === 1) {
    return [nimValues.get(0)];
  }
  const result = [];
  if (number > 2) {
    result.push(nimValues.get(number - 2));
  }
  if (number >= 3) {
    const subtracted = number - 3;
    result.push(nimValues.get(subtracted));
    const halfSubtracted = Math.floor(subtracted / 2);
    if (halfSubtracted >= 1) {
      for (let i = 1; i <= halfSubtracted; i++) {
        const complement = subtracted - i;
        result.push(nimValues.get(i) ^ nimValues.get(complement));
      }
    }
  }
  return result;
};

const mex = (array) => {
  let sorted = array.sort();
  let mex = 0;
  sorted.forEach((element) => {
    if (element === mex) mex++;
  });
  return mex;
};

main();
