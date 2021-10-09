const puppeteer = require('puppeteer');

function Scrape(){
    //launch puppeteer window

    puppeteer.launch({
        headless: true,
        args: [ //opens chromium browser window in background to load page to scrape from
            "--no-sandbox",
            "--disable-gpu",
        ]
    }).then(async chromium => {
        const cTab = await chromium.newPage();
        await cTab.goto("https://boards.4channel.org/v/")
        await cTab.waitForSelector('body');
        //loads webpage and scans html file body

    var post = await cTab.evaluate(() => {
        let sepPost = document.body.querySelectorAll('.postContainer');
        allPosts = [];
        sepPost.forEach((message) => {
            let content = message.querySelector('blockquote').innerText;
            content = content.replace(/(>>\d{9})/g,'')
            content = content.replace('>','')
            content = content.replaceAll('\n','')
            allPosts.push(content)
        });

        return allPosts;
        
    });
        console.log(post);
        await chromium.close();
    }).catch(function(err){
        console.error(err);
    });

}

Scrape();
