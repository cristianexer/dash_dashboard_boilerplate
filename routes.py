from pages import dashboard, analytics, about
from utils.extensions import route


routes = [
    route(name='Dashboard', path='/',
          content=dashboard.content),
    route(name='Analytics', path='/analytics',
          content=analytics.content),
    route(name='About', path='/about',
          content=about.content),
]
