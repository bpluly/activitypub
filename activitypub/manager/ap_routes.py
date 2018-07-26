from .base import app

@app.route("/user/<nickname>", ["GET"])
def route_user(self, nickname):
    #obj = self.database.actors.find(id=nickname)
    obj = self.Actor(id=nickname)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/user/<nickname>/publickey", ["GET"])
def route_publickey(self, nickname):
    obj = self.Actor(id=nickname)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/user/<nickname>/outbox", ["GET"])
def route_user_outbox(self, nickname):
    obj = self.Actor(id=nickname)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/user/<nickname>/outbox/<page>", ["GET"])
def route_outbox_page(self, nickname, page):
    obj = self.Actor(id=nickname)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

#@app.route("/user/<nickname>/outbox", ["POST"])
#def route_(self):
#    return self.render_template("test.html")

@app.route("/user/<nickname>/inbox", ["GET"])
def route_inbox(self, nickname):
    obj = self.Actor(id=nickname)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/user/<nickname>/inbox/<page>", ["GET"])
def route_inbox_page(self, nickname, page):
    obj = self.Actor(id=nickname)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

#@app.route("/user/<nickname>/inbox", ["POST"])
#def route_(self):
#    return self.render_template("test.html")

@app.route("/user/<nickname>/followers", ["GET"])
def route_followers(self, nickname):
    obj = self.Actor(id=nickname)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/user/<nickname>/followers/<page>", ["GET"])
def route_followers_page(self, nickname, page):
    obj = self.Actor(id=nickname)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/user/<nickname>/following", ["GET"])
def route_following(self, nickname):
    obj = self.Actor(id=nickname)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/user/<nickname>/following/<page>", ["GET"])
def route_following_page(self, nickname, page):
    obj = self.Actor(id=nickname)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/user/<nickname>/liked", ["GET"])
def route_liked(self, nickname):
    obj = self.Actor(id=nickname)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/user/<nickname>/liked/<page>", ["GET"])
def route_liked_page(self, nickname, page):
    obj = self.Actor(id=nickname)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/activity/<uuid>", ["GET"])
def route_activity(self, uuid):
    obj = self.manager.Note(id=uuid)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/activity/<uuid>/replies", ["GET"])
def route_activity_replies(self, uuid):
    obj = self.Activity(id=uuid)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/activity/<uuid>/replies/<page>", ["GET"])
def route_activity_replies_page(self, uuid, page):
    obj = self.Activity(id=uuid)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/activity/<uuid>/likes", ["GET"])
def route_activity_likes(self, uuid):
    obj = self.Activity(id=uuid)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/activity/<uuid>/likes/<page>", ["GET"])
def route_activity_likes_page(self, uuid, page):
    obj = self.Activity(id=uuid)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/activity/<uuid>/shares", ["GET"])
def route_activity_shares(self, uuid):
    obj = self.Activity(id=uuid)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/activity/<uuid>/shares/<page>", ["GET"])
def route_activity_shares_page(self, uuid, page):
    obj = self.Activity(id=uuid)
    if obj:
        return self.render_json(
            obj.to_dict()
        )
    else:
        self.error(404)

@app.route("/content/<uuid>", ["GET"])
def route_content(self, uuid):
    return self.render_template(
        "test.html",
        uuid=uuid,
    )

@app.route("/content/<uuid>/replies", ["GET"])
def route_content_replies(self, uuid):
    return self.render_template(
        "test.html",
        uuid=uuid,
    )

@app.route("/content/<uuid>/replies/<page>", ["GET"])
def route_content_replies_page(self, uuid, page):
    return self.render_template(
        "test.html",
        uuid=uuid,
        page=page,
    )

@app.route("/content/<uuid>/likes", ["GET"])
def route_content_likes(self, uuid):
    return self.render_template(
        "test.html",
        uuid=uuid,
    )

@app.route("/content/<uuid>/likes/<page>", ["GET"])
def route_content_likes_page(self, uuid, page):
    return self.render_template(
        "test.html",
        uuid=uuid,
        page=page,
    )

@app.route("/content/<uuid>/shares", ["GET"])
def route_content_shares(self, uuid):
    return self.render_template(
        "test.html",
        uuid=uuid,
    )

@app.route("/content/<uuid>/shares/<page>", ["GET"])
def route_content_shares_page(self, uuid, page):
    return self.render_template(
        "test.html",
        uuid=uuid,
        page=page,
    )
