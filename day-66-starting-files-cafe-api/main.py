from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
import os


TOPSECRETAPIKEY = os.environ.get("TOPSECRETAPIKEY")

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe={
        #Omit the id from the response
        # "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,

        #Put some properties in a sub-category
        "amenities": {
          "seats": random_cafe.seats,
          "has_toilet": random_cafe.has_toilet,
          "has_wifi": random_cafe.has_wifi,
          "has_sockets": random_cafe.has_sockets,
          "can_take_calls": random_cafe.can_take_calls,
          "coffee_price": random_cafe.coffee_price,
        }
    })

@app.route("/all")
def get_all_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc")

    # 1. Ask the database to look for matching cafes immediately
    target_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == query_location)).scalars().all()

    # 2. See if the list contains data or is empty
    if target_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in target_cafes])
    else:
        # 3. If the list is empty, it means the location wasn't found
        return jsonify(error={"NOT FOUND": "Sorry, we don't have a cafe at your location."}), 404


# HTTP POST - Create Record

# 1. Register the route specifically for POST requests
@app.route("/add", methods=["POST"])
def post_new_cafe():
    # 2. Extract values sent from Postman's form body
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )

    # 3. Add to database and commit changes
    db.session.add(new_cafe)
    db.session.commit()

    # 4. Return a success confirmation JSON message
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record

# 1. Register the route for PATCH requests
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_cafe_price(cafe_id):
    # 2. Find the cafe by its ID
    # cafe_to_update = db.get_or_404(Cafe, cafe_id)
    #
    # if cafe_to_update:
    #     # 3. Pull the new price text out from the URL query arguments
    #     cafe_to_update.coffee_price = request.args.get("new_price")
    #     db.session.commit()
    #
    #     # 4. Return success response
    #     return jsonify(response={"success": "Successfully updated the coffee price."}), 200
    # else:
    #     # 5. Handle fallback error if the ID doesn't exist
    #     return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404

    new_price = request.args.get("new_price")
    try:
        cafe = db.get_or_404(Cafe, cafe_id)
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")

    if api_key == TOPSECRETAPIKEY:
        try:
            cafe_to_delete = db.get_or_404(Cafe, cafe_id)
        except AttributeError:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
