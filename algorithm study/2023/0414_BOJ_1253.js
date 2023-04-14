// 좋다

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let n, arr;

rl.question("", function(length) {
  n = parseInt(length);

  rl.question("", function(numbers) {
    arr = numbers.split(' ').map(Number);
    rl.close();
  });
});

const binaryS = (arr, target, i, j)=>{
  let left = 0;
  let right = arr.length-1
  
  while (left <= right) {
    const mid = Math.floor(left + right)
    if (arr[mid]===target) {
      if (![i, j].includes(mid)) return true
      else return false
    } 
    
    else if (arr[mid] < target) {
      left = mid + 1
    }
    else {
      right = mid - 1
    }
  }
  return false
}

rl.on('close', function() {
  const map = new Map()
  const set = new Set()
  
  arr.sort((a,b)=> {
    return a-b
  });
  const max = arr[arr.length-1]
  
  for (let i=0; i<arr.length; i++){
    map.set(arr[i], (map.get(arr[i])||0)+1)

    for (let j=i+1; j<arr.length; j++){
      const sum = arr[i]+arr[j]
      if (sum>max) break;

      const check = binaryS(arr, sum, i, j)
      if (check) set.add(sum)
    }
  }
  // console.log(map)
  // console.log(set)
  let cnt = 0;
  set.forEach(num=>{
    cnt += map.get(num)
  })
  console.log(cnt)
});