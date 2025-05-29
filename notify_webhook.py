import requests

webhook_url = "https://teamroom.nate.com/api/webhook/910f895f/3oQ1GiUSb0Vm4NdyZjI8mWYy"
message = {
    "text": "✅ In-house-Magazine 페이지가 업데이트 되었습니다.\n\n👉 https://agency8group.github.io/In-house-Magazine/\n(깃허브 리포지토리 업데이트 시 자동 발송)"
}

resp = requests.post(webhook_url, json=message)
print("응답코드:", resp.status_code)
print("응답내용:", resp.text)