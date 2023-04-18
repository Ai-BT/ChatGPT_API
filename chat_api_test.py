import openai

# 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
# q
openai.api_key = "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"


model_engine = "text-davinci-002" # 모델 엔진 선택
prompt = "what is your name?" # 질문

# GPT-3 API 호출
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=50,
    temperature=0.7,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0,
    
)

# 결과 출력
print("결과 = ",response.choices[0].text.strip())


# temperature: 생성된 문장의 다양성을 조절하는 파라미터로, 값이 높을수록 보다 다양하고 무작위한 문장이 생성됩니다. 값이 낮을수록 보다 일관성 있는 문장이 생성됩니다.

# n: 생성될 문장의 개수를 지정하는 파라미터입니다. 이 값은 1보다 큰 값을 지정할 수 있습니다. n값이 클수록 여러 개의 문장이 생성됩니다.

# stop: 생성된 문장이 멈출 단어나 구를 지정하는 파라미터입니다. 이를 사용하여 API에서 반환되는 문장의 길이를 제한하거나, 일부분만 출력할 수 있습니다.

# frequency_penalty: 같은 단어가 반복되는 것을 제어하는 파라미터입니다. 값이 높을수록 반복되는 단어의 빈도가 감소합니다.

# presence_penalty: 결과 문장에서 특정 단어가 나타나는 것을 제어하는 파라미터입니다. 값이 높을수록 특정 단어가 나타나는 빈도가 감소합니다.