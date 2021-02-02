#!/usr/bin/node
/*
 *Write a script that prints 3 lines: (like 1-multi_languages.js)
 *but by using an array of string and a loop
 **/
if (!parseInt(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
    occ = parseInt(process.argv[2]);
      for (i = 0; i < occ; i++)
        console.log('C is fun');
}
