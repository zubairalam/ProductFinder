//var request = require('request'),
//    cheerio = require('cheerio'),
//    fs = require('fs'),
//    urls = [];
//
//request('http://www.reddit.com/', function (err, resp, body) {
//    if (!err && resp.statusCode == 200) {
//        var $ = cheerio.load(body);
//        $('.thumbnail').each(function () {
//            var url = $(this).attr('href');
//            console.log(url);
//            if (url.indexOf("jpg") > 0 || url.indexOf("gif") > 0) {
//                urls.push(url);
//            }
//        });
//    }
//    download_images();
//    console.log("this line");
//});
//
//function download_images() {
//    for (var i = 0; i < urls.length; i++) {
//        request(urls[i]).pipe(fs.createWriteStream('img/' + i + '.jpg'));
//        console.log(i);
//    }
//}
//---------------------------------------------------------------------------


// read urls from redis
// extract data
// download image responses
// save image responses in a folder

var redis = require("redis"),
    client = redis.createClient();

client.on("error",function(err){
    console.log("Error" + err);
});

client.lrange("products",0,-1,function(result){
    for (var i=0;i<result.length;i+=1){
        console.log(result[i]);
    }
});

var result = client.lrange("products",0,-1);

console.log(result.length);