import request

res = request.get("https://codedam.com")

print(res.text)
print(res.status_code)