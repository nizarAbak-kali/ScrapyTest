__author__ = 'nizar'
import scrapy


# l'url du site que l'on vas scrapper
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
wikitionary = "https://fr.wiktionary.org/wiki/Wiktionnaire:Liste_de_1750_mots_fran%C3%A7ais_les_plus_courants"
"https://cadres.apec.fr/home/mes-offres/recherche-des-offres-demploi/liste-des-offres-demploi.html?sortsType=DATE&sortsDirection=DESCENDING"


class TestScrapper(scrapy.Spider):
    name = "scrapy"
    allowed_domains = ["cadres.apec.fr"]
    start_urls = [
          "https://cadres.apec.fr/home/mes-offres/recherche-des-offres-demploi/liste-des-offres-demploi.html?sortsType=DATE&sortsDirection=DESCENDING"
          ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

if __name__ == '__main__':
    print("wiki scrapper !!")
