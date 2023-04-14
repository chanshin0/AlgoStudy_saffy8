const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let n;
let set = new Set()

rl.question("", function(length) {
  n = parseInt(length);

  readPipeData();
});

function readPipeData() {
  rl.question("", function(data) {
    const arr = data.split(' ').map((v, idx) => {
      if (idx === 2) v = +v;
      return v;
    });
    set.add(arr);

    if (set.size < n) {
      readPipeData();
    } else {
      rl.close();
    }
  });
}

rl.on('close', function() {
  set = [...set].sort()
  console.log(set)
});
