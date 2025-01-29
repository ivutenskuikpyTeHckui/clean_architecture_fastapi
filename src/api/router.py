from src.api.author import router as router_author
from src.api.book import router as router_book


all_routers = (
    router_author,
    router_book,
) 