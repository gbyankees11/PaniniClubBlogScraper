import urllib2
import re
from BeautifulSoup import BeautifulSoup

namesList = [['Greg'], ['Anthony'], ['Angela'], ['Marc'], ['Trevor'], ['Margo'], ['Mike'], ['Matt', 'Ball'], ['Jeff']]
#namesList = [['Trevor']]

meats = ['pork', 'beef', 'chicken', 'bacon', 'turkey', 'ham', 'prosciutto', 'shrimp', 'eel', 'salami', 'duck', 'lamb', 'sausage']
cheeses = ['cheddar', 'swiss', 'gruyere', 'gouda', 'american', 'mozzarella', 'parmesan', 'blue cheese', 'feta', 'munster', 'jack', 'provolone', 'brie', 'queso', 'goat']
breads = ['white', 'wheat', 'rye', 'pumpernickel', 'cornbread', 'pizza', 'french', 'sourdough', 'ciabatta']
other = ['olives', 'lettuce', 'avocado', 'pepper', 'hot sauce', 'garlic', 'basil', 'capers', 'butter', 'onion', 'honey', 'vinegar', 'capers', 'aioli', 'mayo', 'tomato', 'cilantro', 'rosemary', 'thyme', 'jalepeno', 'scallions', 'shallot', 'ginger', 'cucumber', 'siracha', 'apple', 'mushroom', 'cauliflower', 'egg']

allIngredients = {}
allIngredients['meats'] = meats
allIngredients['cheeses'] = cheeses
allIngredients['breads'] = breads
allIngredients['other'] = other

class Panini:
  def __init__(self, url, author, scores, ingredients):
    self.url = url
    self.author = author
    self.scores = scores
    self.ingredients = ingredients

  def __str__(self):
    string = 'Url: ' + self.url
    string += 'Author: ' + self.author + '\n'
    string += '\n'
    string += 'Scores:' + '\n'
    for scorer in self.scores:
      string += scorer + ': ' + str(self.scores[scorer]) + '\n'
    string += '\n'
    for ingredientType in self.ingredients:
      string += ingredientType + ': ' + str(self.ingredients[ingredientType]) + '\n'

    return string


def scrapeBlog():
  print 'scraping...'
  urls = open('urls.txt')

  paninis = []

  for url in urls:
    print url
    resp = urllib2.urlopen(url)
    html = resp.read()
    authorRegex = '<a class="author-link".*?>(.*)</a>'
    authorMatch = re.search(authorRegex, html)
    paninis.append(Panini(url, authorMatch.group(1), getScores(html), getIngredients(html)))

  return paninis


def getScores(html):

  scores = {}

  for names in namesList:
    for name in names:
      scoreRegex = name + '(?: )?[:-]?[(?: )(?:&nbsp;)]*([0-9,]{6,7})'
      scoreMatch = re.search(scoreRegex, html, flags=re.IGNORECASE)

      if scoreMatch:
        scores[names[0]] = int(scoreMatch.group(1).replace(',', ''))
        break

  return scores

def ingredientRegex(ing):
  return '[> \n]' + ing + '[< s)\n]'

def getIngredients(html):
  ingredients = {}

  blogPostContent = BeautifulSoup(html).body.find('div', attrs={'class':'blog-section'}).prettify()

  for ingredientType in allIngredients:
    ingredients[ingredientType] = []
    for ingredient in allIngredients[ingredientType]:
      regex = ingredientRegex(ingredient)
      if re.search(regex, blogPostContent, re.IGNORECASE):
        ingredients[ingredientType].append(ingredient)

  return ingredients

