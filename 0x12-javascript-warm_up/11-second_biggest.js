#!/usr/bin/node
/*
 *script that searches the second biggest integer in the list of arguments
 **/
if (process.argv.length === 2 || process.argv.length === 3) {
    console.log(0);
} else {
    Tab = process.argv.slice(2);
    Tab.sort();
    console.log(Tab.length - 2);
}


