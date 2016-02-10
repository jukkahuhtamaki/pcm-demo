// http://www.tut.fi/wwwoppaat/opas2015-2016/perus/laitokset/

var casper = require('casper').create({
  verbose: true,
  clientScripts: ['includes/jquery-2.1.3.js'] 
});
var fs = require('fs');
var clicks = 0;
var x = require('casper').selectXPath; 
casper.start('https://www.indiegogo.com/projects/jolla-tablet-world-s-first-crowdsourced-tablet#/funders');