#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const storageFile = process.argv[3];
request(url).pipe(fs.createWriteStream(storageFile));
