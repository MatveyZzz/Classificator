import requests


def cleaner(n: str) -> str:
    junk = ["<p>", "</p>", "<ul>", "</ul>", "\\r\\n", "<li>", "</li>", "\\r\\n\\r\\n", "\xa0"]
    for junkpiece in junk:
        n = n.replace(junkpiece, "")
    n = n.replace("\n", " ")
    return n


reviews = {}
for page in range(1,3,1):
    url = f"https://www.banki.ru/services/responses/list/ajax/?page={page}&type=all&bank=promsvyazbank"
    response = requests.get(url).json()
    data = response["data"]
    for i in data:
        print(i)

    j = 0
    for i in data:
        tmp = data[j]
        name = tmp["id"]
        text = cleaner(tmp["text"])
        reviews[name] = text
        j += 1

print("===============================")

for i in reviews:
    print(f"{i}: {reviews[i]}")
