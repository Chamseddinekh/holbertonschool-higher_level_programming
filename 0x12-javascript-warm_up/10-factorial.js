#!/usr/bin/node
/*
 *script that computes and prints a factorial
 **/
let a = parseInt(process.argv[2]);
function Fact(a)
{
if (a <= 1 || a === NaN) {
return 1;
} else { 
  return a * Fact( a - 1 );
}
}
console.log(Fact(a));