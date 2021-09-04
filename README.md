# Advanced web scraping & crawling using Scrapy & Splash
Built a Desktop app using Tkinter, the app will fetch &amp; execute the spiders in my Scrapy project

Bypass Google ReCaptcha(a technique used to fool websites and let them think that the request is sent using a browser & was performed by a human being!)

Built clean & well-structured spiders.

Heavy data processing, Input & Output processors work in order to clean the scraped data points as this will ensure the quality of our feeds.

Desktop app using Tkinter,the app will fetch & execute all the available spiders in our Scrapy project, we can also choose the feed type, feed location & name, 
this is also extremely helpful 

The website from which i scraped is [zillow](https://www.zillow.com)

The Desktop app Screenshot i obtained after executing the code:

[![Product Name Screen Shot][product-screenshot]](https://www.linkpicture.com/q/desktop_app_tkinter.jpg)

[product-screenshot]: desktop_app_tkinter.jpg

We can choose the feed as json or CSV and accordingly in the output data will be in the chosen format. Here only one spider exists which is zillow_houses.The code is written in zillow/spiders/zillow_houses.py

And in the Browse row ,  we can select the destination folder and name the file(say as dataset) in the 2nd box and click Execute.The code gets executed and you can search the destination folder and go to the given file name(dataset) and you get the output file desired.

