import requests

# FastAPI 엔드포인트 api
API_URL = "http://172.16.213.22:8000/gpt"


def getResponse(leader, role, repositoryUrl, additional_desc):
    payload = {
        "resposUrl": repositoryUrl,
        "role": role,
        "extra_info": additional_desc,
        "leader": True
    }
    print(payload)
    # POST 요청 보내기
    response = requests.post(API_URL, json=payload)
    print(response.status_code)
    # 서버에서 받은 응답 출력
    return response.json()
