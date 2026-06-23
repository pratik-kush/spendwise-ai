
def generate_advice(total_expense, top_category):

    if top_category == "Food":
        return "You are spending too much on food delivery. Try cooking more."
    elif top_category == "Shopping":
        return "Shopping expenses are high. Avoid unnecessary purchases."
    elif top_category == "Subscription":
        return "You have many subscriptions. Consider canceling unused ones."
    else:
        return "Your spending is stable. Keep tracking your expenses."
