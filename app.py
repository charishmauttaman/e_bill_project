from flask import Flask, render_template, request
from logic import predict_bill, give_suggestions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    bill = None
    suggestions = []
    usage_data = {}

    if request.method == "POST":
        units = int(request.form["units"])
        members = int(request.form["members"])

        ac = int(request.form["ac"])
        fan = int(request.form["fan"])
        fridge = int(request.form["fridge"])
        washing = int(request.form["washing"])
        tv = int(request.form["tv"])

        wfh = 1 if request.form["wfh"] == "yes" else 0
        geyser = 1 if request.form["geyser"] == "yes" else 0
        festival = 1 if request.form["festival"] == "yes" else 0
        summer = 1 if request.form["summer"] == "yes" else 0

        bill = predict_bill(
            units, ac, fan, fridge, members,
            washing, tv, wfh, geyser,
            festival, summer
        )

        suggestions = give_suggestions(ac, fan, fridge, units)

        # Data for graphs
        usage_data = {
            "AC": ac,
            "Fan": fan,
            "Refrigerator": fridge,
            "TV": tv,
            "Washing Machine": washing
        }

    return render_template(
        "index.html",
        bill=bill,
        suggestions=suggestions,
        usage_data=usage_data
    )

if __name__ == "__main__":
    app.run(debug=True)
