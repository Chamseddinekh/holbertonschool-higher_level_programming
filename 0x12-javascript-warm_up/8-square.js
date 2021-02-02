#!/usr/bin/node
/*
 *script that prints a square
 **/
if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  x = parseInt(process.argv[2]);
  for (let i = 0; i < x; i++) 
    console.log('X'.repeat(x));
}
  