from aiohttp import web
app = web.Application()
app.router.add_static(expect_handler=None, prefix='/static/', path='./')
