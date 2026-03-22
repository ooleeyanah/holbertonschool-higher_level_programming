#!/usr/bin/node
const size = process.argv[2];
const number = parseInt(size);

if (isNaN(number)) {
  console.log('Missing size');
} else if (number > 0) {
  for (let i = 0; i < number; i++) {
    let row = '';
    for (let j = 0; j < number; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
