from randomusers import randomusers_data

def get_email_list(users: list[dict]) -> list[str]:
    emails = []
    for user in users:
        emails.append(user['email'])
    return emails


def get_name_list(users: list[dict]) -> list[str]:
    names =[]
    for user in users :
        names.append(user["name"])
    return names


def get_country_list(users: list[dict]) -> list[str]:
     countrys = []
     for user in users :
        countrys.append(user["location"]["country"])
        return countrys

def get_phone_list(users: list[dict]) -> list[str]:
    phones=[]
    for user in users :
        phones.append(user["phone"])
        return phones

def get_city_list(users: list[dict]) -> list[str]:
    citys=[]
    for user in users :
        citys.append(user["location"]["city"])
        return citys



def get_oldest_user(users: list[dict]) -> dict:
    oldests=[]
    for user in users :
        oldests.append(user["dob"]["age"])
    return oldests


def get_youngest_user(users: list[dict]) -> dict:
    youngests=[]
    for user in users :
        youngests.append(user["dob"]["age"])
    return youngests




def main() -> None:


results = randomusers_data["results"]
email_list = get_email_list(results)
print(email_list)


phones=randomusers_data["results"]
phone_list=get_phone_list(phones)
print(phone_list)

names=randomusers_data["results"]
name_list = get_name_list(names)
print(name_list)


countrys=randomusers_data["results"]
country_list=get_country_list(countrys)
print(country_list)


citys=randomusers_data["results"]
city_list = get_city_list(citys)
print(city_list)


oldests=randomusers_data["results"]
oldest_list=get_oldest_user(oldests)
print(max(oldest_list))


youngests=randomusers_data["results"]
youngest_list=get_youngest_user(oldests)
print(min(youngest_list))


if __name__ == "__main__":
    main()