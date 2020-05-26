from pages import dashboard, analytics, contact
from utils.extensions import route


routes = [
    route(name='Dashboard', path='/',
          content=dashboard.content),
    route(name='Analytics', path='/analytics',
          content=analytics.content),
    route(name='Contact', path='/contact',
          content=contact.content),
]
