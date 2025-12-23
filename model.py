import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
df=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\e_bill\electricity_bill_dataset.csv")
df.head()
df.info()
TARGET = "ElectricityBill"
features = [
    "Fan",
    "Refrigerator",
    "AirConditioner",
    "Television",
    "Monitor",
    "MotorPump",
    "MonthlyHours",
    "TariffRate"
]

X = df[features]
y = df[TARGET]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", mae)
def predict_bill(units, ac, fan, fridge, members,
                 washing, tv, wfh, geyser, festival, summer):

    bill = units * 6   # base unit rate

    bill += ac * 60
    bill += fan * 10
    bill += fridge * 5
    bill += members * 30
    bill += washing * 40
    bill += tv * 8

    if wfh:
        bill += 200
    if geyser:
        bill += 250
    if festival:
        bill += 300
    if summer:
        bill += 400

    return bill
    def give_suggestions(ac, fan, fridge, units):
    tips = []

    # AC related
    if ac > 6:
        tips.append("Reduce AC usage or keep temperature at 24–26°C.")
        tips.append("Use ceiling fans along with AC to improve cooling efficiency.")
        tips.append("Clean AC filters regularly to reduce power consumption.")

    # Fan related
    if fan > 10:
        tips.append("Turn off fans when rooms are not in use.")
        tips.append("Use energy-efficient BLDC fans.")

    # Refrigerator related
    if fridge > 24:
        tips.append("Avoid frequent refrigerator door opening.")
        tips.append("Do not overload the refrigerator.")
        tips.append("Set refrigerator temperature to optimal level (3–5°C).")

    # High consumption warning
    if units > 300:
        tips.append("High electricity usage detected. Consider performing an energy audit.")
        tips.append("Replace old appliances with 5-star rated appliances.")
        tips.append("Check for power leakage or faulty wiring.")

    if units > 500:
        tips.append("Very high electricity consumption detected. Solar panels may reduce long-term costs.")

    # General energy saving tips
    tips.append("Switch off appliances when not in use.")
    tips.append("Use LED bulbs instead of CFL or incandescent bulbs.")
    tips.append("Unplug chargers and devices when fully charged.")
    tips.append("Use natural sunlight during daytime.")
    tips.append("Iron clothes in bulk to reduce repeated heating.")

    return tips
    def ask_questions():
    print("Answer these questions so I can predict your electricity bill:\n")

    # Basic usage
    units = int(input("How many units did you consume this month? "))
    members = int(input("How many members are living in your house? "))

    # Appliance usage
    ac = int(input("How many hours per day do you use AC? "))
    fan = int(input("How many hours per day do you use fans? "))
    fridge = int(input("How many hours per day do you use refrigerator? "))
    washing = int(input("How many times per week do you use washing machine? "))
    tv = int(input("How many hours per day do you use TV? "))

    # Lifestyle
    wfh = input("Is anyone working or studying from home? (yes/no): ").lower()
    geyser = input("Do you use geyser daily? (yes/no): ").lower()

    # Events & seasons
    festival = input("Is there any festival or special event this month? (yes/no): ").lower()
    summer = input("Is it a summer month? (yes/no): ").lower()

    # Convert yes/no to numbers
    wfh_flag = 1 if wfh == "yes" else 0
    geyser_flag = 1 if geyser == "yes" else 0
    festival_flag = 1 if festival == "yes" else 0
    summer_flag = 1 if summer == "yes" else 0

    # Prediction
    bill = predict_bill(
        units, ac, fan, fridge, members,
        washing, tv, wfh_flag, geyser_flag,
        festival_flag, summer_flag
    )

    # Suggestions
    suggestions = give_suggestions(units, ac, geyser_flag, summer_flag)

    print("\n---------------------------------------")
    print(f"Estimated Electricity Bill: ₹{bill:.2f}")
    print("Suggestions:")
    for s in suggestions:
        print("-", s)
    print("---------------------------------------")
    import matplotlib.pyplot as plt

df.hist(figsize=(12,8))
plt.suptitle("Dataset Distribution of Electricity Features")
plt.show()
plt.figure()
plt.plot(df["ElectricityBill"])
plt.title("Monthly Electricity Bill Trend")
plt.xlabel("Households / Months")
plt.ylabel("Electricity Bill (₹)")
plt.show()
appliances = ["Fan", "Refrigerator", "AirConditioner", "Television"]

plt.figure()
df[appliances].mean().plot(kind="bar")
plt.title("Average Appliance Usage")
plt.ylabel("Usage")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
appliances = [
    "Fan", "Refrigerator", "AirConditioner",
    "Television", "Monitor", "MotorPump"
]

plt.figure()
df[appliances].mean().plot(kind="bar")
plt.title("Average Appliance Usage")
plt.ylabel("Average Usage")
plt.xlabel("Appliances")
plt.show()

plt.figure()
plt.scatter(df["MonthlyHours"], df["ElectricityBill"])
plt.xlabel("Monthly Usage Hours")
plt.ylabel("Electricity Bill (₹)")
plt.title("Monthly Hours vs Electricity Bill")
plt.show()
plt.figure()
plt.plot(df["TariffRate"], df["ElectricityBill"])
plt.xlabel("Tariff Rate")
plt.ylabel("Electricity Bill (₹)")
plt.title("Tariff Rate vs Electricity Bill")
plt.show()

city_bill = df.groupby("City")["ElectricityBill"].mean()

plt.figure()
city_bill.plot(kind="bar")
plt.xlabel("City")
plt.ylabel("Average Electricity Bill (₹)")
plt.title("City-wise Average Electricity Bill")
plt.show()

plt.figure()
df.boxplot(column="ElectricityBill", by="Company")
plt.title("Electricity Bill Distribution by Company")
plt.suptitle("")
plt.xlabel("Company")
plt.ylabel("Electricity Bill (₹)")
plt.show()
plt.figure()
plt.scatter(df["AirConditioner"], df["ElectricityBill"])
plt.xlabel("Air Conditioner Usage")
plt.ylabel("Electricity Bill (₹)")
plt.title("AC Usage vs Electricity Bill")
plt.show()
monthly_avg = df.groupby("Month")["ElectricityBill"].mean()

plt.figure()
monthly_avg.plot()
plt.xlabel("Month")
plt.ylabel("Average Electricity Bill (₹)")
plt.title("Monthly Electricity Bill Trend")
plt.show()