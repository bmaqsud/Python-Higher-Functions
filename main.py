from randomusers import randomusers_data

def get_email_list(users: list[dict]) -> list[str]:
    "Get list of email addresses from users"
    emails = []
    for user in users:
        emails.append(user['email'])
    return emails

results = randomusers_data["results"]
email_list = get_email_list(results)
print(email_list)

def get_name_list(users: list[dict]) -> list[str]:
    names =[]
    for user in users :
        names.append(user["name"])
    return names

names=randomusers_data["results"]
name_list = get_name_list(names)
print(name_list)
def get_country_list(users: list[dict]) -> list[str]:
     countrys = []
     for user in users :
        countrys.append(user["location"]["country"])
        return countrys

countrys=randomusers_data["results"]
country_list=get_country_list(countrys)
print(country_list)

def get_phone_list(users: list[dict]) -> list[str]:
    phones=[]
    for user in users :
        phones.append(user["phone"])
        return phones

phones=randomusers_data["results"]
phone_list=get_phone_list(phones)
print(phone_list)
def get_city_list(users: list[dict]) -> list[str]:
    citys=[]
    for user in users :
        citys.append(user["location"]["city"])
        return citys

citys=randomusers_data["results"]
city_list = get_city_list(citys)
print(city_list)

def get_oldest_user(users: list[dict]) -> dict:
    oldests=[]
    for user in users :
        oldests.append(user["dob"]["age"])
    return oldests

oldests=randomusers_data["results"]
oldest_list=get_oldest_user(oldests)
print(max(oldest_list))

def get_youngest_user(users: list[dict]) -> dict:
    youngests=[]
    for user in users :
        youngests.append(user["dob"]["age"])
    return youngests

youngests=randomusers_data["results"]
youngest_list=get_youngest_user(oldests)
print(min(youngest_list))


def main() -> None:
    print("hech narsa")

if __name__ == "__main__":
    main()