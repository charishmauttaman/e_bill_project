def predict_bill(units, ac, fan, fridge, members,
                 washing, tv, wfh, geyser,
                 festival, summer):

    bill = (
        units * 6 +
        ac * 150 +
        fan * 20 +
        fridge * 30 +
        washing * 50 +
        tv * 10 +
        members * 40 +
        wfh * 100 +
        geyser * 120 +
        festival * 200 +
        summer * 300
    )

    return bill


def give_suggestions(ac, fan, fridge, units):
    tips = []

    if ac > 6:
        tips.append("Reduce AC usage or keep temperature at 24–26°C.")
        tips.append("Use ceiling fans along with AC to improve cooling efficiency.")
        tips.append("Clean AC filters regularly to reduce power consumption.")

    if fan > 10:
        tips.append("Turn off fans when rooms are not in use.")
        tips.append("Use energy-efficient BLDC fans.")

    if fridge > 24:
        tips.append("Avoid frequent refrigerator door opening.")
        tips.append("Do not overload the refrigerator.")
        tips.append("Set refrigerator temperature to optimal level (3–5°C).")

    if units > 300:
        tips.append("High electricity usage detected. Consider energy audit.")
        tips.append("Replace old appliances with 5-star rated appliances.")

    if units > 500:
        tips.append("Solar panels can reduce long-term electricity costs.")

    tips.append("Switch off appliances when not in use.")
    tips.append("Use LED bulbs.")
    tips.append("Unplug chargers when not needed.")

    return tips