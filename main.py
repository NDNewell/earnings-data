from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import Column, String, Date, Float, DateTime, func

app = Flask(__name__)
# SQLAlchemy Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://us_admin:admin@localhost/earnings"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
# Marshmallow Configuration
ma = Marshmallow(app)


# Model definition
class Earnings(db.Model):
    id = Column(String, primary_key=True, autoincrement=False)
    url = Column(String)
    origin = Column(String)
    destination = Column(String)
    duration = Column(String)
    distance = Column(String)
    vehicle_type = Column(String)
    time_requested = Column(String)
    date_requested = Column(Date)
    fare = Column(Float)
    surge = Column(Float)
    wait_time = Column(Float)
    tip = Column(Float)
    adjustment = Column(Float)
    priority = Column(Float)
    reservation_fee = Column(Float)
    service_fee = Column(Float)
    booking_fee_deduction = Column(Float)
    booking_fee_payment = Column(Float)
    pet_surcharge = Column(Float)
    cancellation_fee = Column(Float)
    earnings = Column(Float)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


# Schema definition
class EarningsSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "url",
            "origin",
            "destination",
            "duration",
            "distance",
            "vehicle_type",
            "time_requested",
            "date_requested",
            "fare",
            "surge",
            "wait_time",
            "tip",
            "adjustment",
            "priority",
            "reservation_fee",
            "service_fee",
            "booking_fee_deduction",
            "booking_fee_payment",
            "pet_surcharge",
            "cancellation_fee",
            "earnings",
            "created_at",
            "updated_at",
        )


earnings_schema = EarningsSchema()  # Single earning
earnings_schema_list = EarningsSchema(many=True)  # Multiple earnings


@app.route("/earnings", methods=["GET"])
def get_all_earnings():
    all_earnings = Earnings.query.all()
    return earnings_schema_list.jsonify(all_earnings)


@app.route("/earnings/<string:id>", methods=["GET"])
def get_earning_by_id(id):
    earning = Earnings.query.get(id)
    if earning:
        return earnings_schema.jsonify(earning)
    else:
        return jsonify({"error": "Earning not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
