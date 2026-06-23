
def classify_transaction(description):
    description = description.lower()

    if "swiggy" in description or "zomato" in description:
        return "Food"
    elif "amazon" in description or "flipkart" in description:
        return "Shopping"
    elif "uber" in description or "ola" in description:
        return "Travel"
    elif "netflix" in description or "spotify" in description:
        return "Subscription"
    elif "electricity" in description or "water" in description:
        return "Bills"
    elif "rent" in description:
        return "Rent"
    elif "movie" in description:
        return "Entertainment"
    elif "stock" in description or "mutual" in description:
        return "Investment"
    else:
        return "Other"
