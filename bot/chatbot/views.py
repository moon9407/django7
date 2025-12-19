import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI


def get_openai_client():
    return OpenAI()
def index(request):
    return render(request, "chatbot/index.html")


@csrf_exempt
def chat_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"})

    data = json.loads(request.body)
    user_message = data.get("message", "")
    history = data.get("history", [])

    messages = [
        {
            "role": "system",
            "content": "너는 민원 접수를 돕는 공공기관 챗봇이다. 정중하고 간결하게 답변해라."
        }
    ] + history

    messages.append({"role": "user", "content": user_message})

    # ✅ 여기서 생성
    client = get_openai_client()

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    return JsonResponse({
        "reply": response.choices[0].message.content
    })