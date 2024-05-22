# Notes
Create spider class with name, allowed_domain, start_urls and parse(response). you can extract elements using css selector, and then return it or store it in item. then after running crawler it will generate desired output.


# CSS Selector
```
response.css("title") # tag inside HTML
response.css("title").extract() # 
response.css("title::text").extract()
response.css("title::text")[0].extract()
response.css("title::text").extract_first()
response.css("span.text::text") # extract span element with class="text" using .
response.css("span#text::text") # extract span element with id="text" using #

Selector Gadget - chrome extension
    - select element you want to select, click other to deselect elements

response.css(".author::text").extract()
```

Run Spider
```
scrapy crawl <spider_name>

# run spider and store data as json
scrapy crawl puma -O puma.json

# store data as csv (final output)
scrapy crawl puma -O puma.csv
```

# Learn
- xpath, css syntax for scraping
    - https://testsigma.com/blog/xpath-vs-css-selector/
