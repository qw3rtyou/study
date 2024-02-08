const puppeteer = require('puppeteer')
const crypto    = require('crypto');
const fs        = require('fs'); 


const flag = fs.readFileSync("/flag.txt").toString();
const baseurl = "localhost:8000";

async function visit(uid) {
    const browser = await puppeteer.launch({
        args: [
            "--no-sandbox",
            "--headless"
        ],
        executablePath: '/usr/bin/google-chrome'
    })
    try {
        let page = await browser.newPage()

        await page.goto(`http://${baseurl}/login`)

        await page.waitForSelector('#username')
        await page.focus('#username')
        await page.keyboard.type(crypto.randomBytes(10).toString(), { delay: 10 })

        await page.waitForSelector('#password')
        await page.focus('#password')
        await page.keyboard.type(crypto.randomBytes(20).toString(), { delay: 10 })

        await new Promise(resolve => setTimeout(resolve, 300))
        await page.click('#submit')
        await new Promise(resolve => setTimeout(resolve, 300))

        page.setCookie({
            "name": "FLAG",
            "value": flag,
            "domain": baseurl,
            "path": "/",
            "httpOnly": false,
            "sameSite": "Strict"
        })

        await page.goto(`http://${baseurl}/share/read/${uid}`, { timeout: 5000 })
        await new Promise(resolve => setTimeout(resolve, 5000))
        await page.close()
        await browser.close()
    } catch (e) {
        console.log(e)
        await browser.close()
    }

}

module.exports = { visit }
