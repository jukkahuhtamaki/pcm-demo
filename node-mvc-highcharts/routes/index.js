var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  var data = {
      list: ['one', 'two', 'tree']
  };
  console.log(data);    
    
  res.render('index', { title: 'Hello?', foo: 'Foo', data: data });
});

module.exports = router;
