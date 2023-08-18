import advertools as adv
from advertools import crawl
import pd
urls = [
    "https://friv.com/",
    "https://lottie.com/",
    "https://minerva.com/",
    "https://sockshop.co.uk/",
    "https://nottinghamforest.co.uk/",
    "https://seekingalpha.com/",
    "https://gem-a.com/",
    "https://microsoft.com/",
    "https://apple.com/",
    "https://west-quay.co.uk/",
    "https://johnlewis.com/",
    "https://blackopaldirect.com/"
]

crawl(urls, 'output.jl', follow_links=True)

