# Scrape the panini club blog!

```
>>> import panini
>>> paninis = panini.scrapeBlog()
scraping...
http://paniniclub.biz/trevor-week-42

http://paniniclub.biz/bbq-pork-slaw-sauteed-apple-greg-43

http://paniniclub.biz/sausage-and-peppers-marc-week-44

...
...

>>> print paninis[2]
Url: http://paniniclub.biz/sausage-and-peppers-marc-week-44
Author: Marc Neuwirth

Scores:
Matt: 825000
Marc: 951200
Jeff: 938333
Trevor: 920000
Greg: 851499
Angela: 949620
Margo: 925002

cheeses: ['provolone']
other: ['pepper', 'garlic', 'onion']
meats: ['sausage']
breads: ['ciabatta']

>>>
```

