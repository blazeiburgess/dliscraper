from scraper import Scraper
from tqdm import tqdm

LANGUAGES = [
    "spanish",
    "chinese",
    "english",
    "japanese",
    "french",
    "korean",
    "german",
    "russian",
    "italian",
    "arabic",
    "portuguese",
]

def main():
    for language in tqdm(LANGUAGES):
        scraper = Scraper(language)
        scraper.scrape()

if __name__ == '__main__':
    main()
