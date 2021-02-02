#!/usr/bin/node
/*
 *script that searches the second biggest integer in the list of arguments
 **/
let Tab = process.argv.slice(2);
if (Tab.length <= 1) {
    console.log(0);
} else {
    Tab.sort();
    console.log(Tab[Tab.length - 2]);
}


