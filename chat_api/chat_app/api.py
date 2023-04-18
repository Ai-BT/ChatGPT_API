
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from rest_framework.decorators import action
from django.http import HttpResponse, JsonResponse
import openai


class UserCheck(APIView):
    queryset = Users.objects.all()

    def get_queryset(self):
        return Users.objects.all()

    def post(self, request):
        inputUserId = request.data.get("userPhone")
        print("phone number = ",inputUserId)
        
        get_user = self.queryset.get(userPhone=inputUserId)
        # print(get_user.userName)

        if get_user.userType == 'U':
            responsedata = dict(msgCode=200, msg="find user", userPhone=inputUserId, userName = get_user.userName, userTF=True)
            return JsonResponse(responsedata) 

        return Response(status.HTTP_400_BAD_REQUEST)
    

class Chatgpt(APIView):
    def post(self, request):
        openai.api_key = "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"

        question = request.data.get("question")

        model_engine = "text-davinci-002" # 모델 엔진 선택
        prompt = question

        # GPT-3 API 호출
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=50
        )

        result = response.choices[0].text.strip()

        responsedata = dict(msgCode=200, msg="chat gpt", result = result)
        return Response(responsedata)
    


#     import openai

# # api key = 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
# openai.api_key = "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"


# model_engine = "text-davinci-002" # 모델 엔진 선택
# prompt = "안녕하세요"

# # GPT-3 API 호출
# response = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=500
# )

# # 결과 출력
# print("답변 = ",response.choices[0].text.strip())