import responder

api = responder.API()

@api.route("/{slug}")
async def greet_world(req, resp, *, slug):
    resp.text = f"{slug}, world!"

if __name__ == '__main__':
    api.run()
