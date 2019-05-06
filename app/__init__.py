from flask import Flask

def create_app(config='app.config.Config'):
  app = Flask(__name__)
  # app.wsgi_app = ReverseProxied(app.wsgi_app)
  app.config.from_object(config)

  with app.app_context():
    from app.views import views
    app.register_blueprint(views)

  return app


  