var mysql   = require('mysql');
var connection = mysql.createConnection({
 host   : 'localhost',
 user   : 'root',
 password : '111111',
 database : 'users'
});

connection.connect();

var  sql = 'SELECT * FROM images';

connection.query(sql, function(err, result) {
 if (err) {
  console.log('[SELECT ERROR] - ', err.message);
  return;
 };

 console.log('The solution is: ', result);
});

connection.end();
