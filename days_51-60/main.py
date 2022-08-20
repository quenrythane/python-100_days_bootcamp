import requests as req


url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = req.get(url).json()

index = 2

post_data = blog_response[index-1]

print(post_data)
print(post_data["title"])
# print(post_data.body)
