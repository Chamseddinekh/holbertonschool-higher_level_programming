#!/usr/bin/node
/*
 *script that computes and prints a factorial
 **/
let a = parseInt(process.argv[2]);
function Fact(a)
{
if (isNaN(a) || a <= 1) {
return 1;
} else { 
  return a * Fact( a - 1 );
}
}
console.log(Fact(a));
