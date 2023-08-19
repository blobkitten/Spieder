import advertools as adv
from advertools import crawl
import pandas as pad
urls = [
    "https://friv.com/",
    "https://lottie.com/",
    "https://minerva.com/",
    "https://nottinghamforest.co.uk/",
    "https://seekingalpha.com/",
    "https://gem-a.com/",
    "https://www.microsoft.com/en-gb/",
    "https://apple.com/",
    "https://west-quay.co.uk/",
    "https://johnlewis.com/",
    "https://blackopaldirect.com/"
]

crawl(urls, 'output.jl', follow_links=True)

crawl_df = pad.read_json('output.jl', lines=True)
crawl_df.to_excel('output.xlsx', index=False)