# Flipkart Clone

Built a server side app that it a clone of e-commerce websites and tries to respond to some of the request that would be sent to the server of an e-commerce website. 

## Functionalities

With the app, you can add users as Admin, Owners, normal users. Owners can add products with product metadata and select the category, users can search for items by name, category, Add products to cart, order products in the cart, and also add products to the wishlist. Users can comment on a product also upvote or downvote a product.

## Starting the server

1)After cloning, Change directory on the terminal the folder and activate the virtual environment. The virtual environment contains all the dependencies required for the project such as Flask, Flask-SQLAlchemy, Flask-Migrate.following command is for windows OS 

```bash
//to activate the virtual environment//
flipkart_env\scripts\activate

//to start the server//
set FLASK_ENV=development
set FLASK_APP=server.py
flask run
```

2)To set up the configuration for MySQL access. Open the [init.py](http://init.py) file inside the main folder within the app folder(app>main>__init__.py). You will have to update the password and the database name. Currently, the database name is "f*lipkart"*

```python
database_password = os.environ.get("DB_PASS")
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:%s@localhost/flipkart"%(database_password)
```

3)The model's folder contains all the details related tables for the database. You can make changes to the existing models and add models in this folder. To migrate the models to the database using the following command on the terminal.

```bash
flask db init
flask db migrate
flask db upgrade
```
