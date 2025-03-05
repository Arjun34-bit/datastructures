//Thirs biggest element in array
// [21,54,2,32,1,24,5]  result = 24

const tLargest = (arr) => {
  let largest = -1;
  let secondLargest = -1;
  let thirdLargest = -1;

  for (let i = 0; i <= arr.length; i++) {
    if (arr[i] > largest) {
      thirdLargest = secondLargest;
      secondLargest = largest;
      largest = arr[i];
    } else if (
      arr[i] < secondLargest &&
      arr[i] != largest &&
      arr[i] > thirdLargest
    ) {
      thirdLargest = arr[i];
    } else if (arr[i] > secondLargest && arr[i] != largest) {
      secondLargest = arr[i];
    }
  }
  return thirdLargest;
};

console.log(tLargest([21, 54, 2, 32, 1, 24, 5]));
console.log(tLargest([1, 2, 3]));
console.log(tLargest([10, 5, 0, 65, 4]));
