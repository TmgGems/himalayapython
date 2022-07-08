properties=[
    "profiles":[
    {
        "name":"Ram",
        "rank":1,
        "contact":["9845412345","9818639881"]
    },
    {
    "name":"Sita",
    "rank":2,
    "contact":["9434436","98574785"]    
    }
]
},
"total count":2,
}
profiles=properties.get("data").get("profiles")
for profile in profiles:
    print("**********************")
    print(f"Name:{profile.get('name')}")
    print(f"Rank:{profile.get('rank')}")
    for idx,contact in enumerate(profile.get("contact"),1):
        print(f"Contact{indx}:{contact}")
# OUTPUT
# ***********
# Name:Ram
# Rank:1
# Contact1:
# contact2:
# ***********
# Name:Sita
# Rank:2
# Contact1:
# contact2: