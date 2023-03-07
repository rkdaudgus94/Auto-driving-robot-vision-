# 주어진 문자열 분리
# 주어진 문자열과 위치 리스트
text = "613으로 가줘, 누구한테 물건을 어디로 갖다줘"
location = ['으로', '로', '이에게', '에게', '을', '를', '이한테' '한테', '에']

# 문자열을 띄어쓰기 기준으로 분리
text = text.split()

#count = 0

# 1 조사가 포함된 단어 찾기
#for word in text :
#    for loc in location:
#        if loc in word:
#            print(word)
#            count = count + 1
#            break
#print('찾은 단어의 개수 =', count)


# 2 조사가 포함된 단어를 찾은 후 조사 제거
#for word in text :
#    found_loc = [loc for loc in location if loc in word]
#    if found_loc :
#        for loc in found_loc :
#            word = word.replace(loc, '')
#        print(word)


# 3 조사가 포함된 단어를 찾은 후 조사 제거 후 문자열로 저장
# 결과를 저장할 빈 문자열
#result = ''

# 각 단어에 대해 위치 리스트에 포함된 단어가 있으면
#for word in text :
#    found_loc = [loc for loc in location if loc in word]
    #  위치 리스트에 포함된 단어가 있으면 해당 위치 단어를 삭제하고 결과를 문자열에 저장
#    if found_loc :
#        for loc in found_loc:
#            word = word.replace(loc, '')
#        result += word + " "

# 삭제한 단어 저장
#result = result.strip()
#print(result)
#print(type(result))


# 4 조사가 포함된 단어를 찾은 후 조사 제거 후 리스트로 저장
# location 단어가 포함된 단어들을 저장할 리스트
result = []

# 문자열을 순회하면서 location이 포함된 단어를 찾음
for word in text :
    for loc in location :
        if loc in word :
            # location의 단어를 제거한 후 저장
            result.append(word.replace(loc, ""))
            # 613으로 같은 경우 '으로'와 '로'가 포함되어 2번 결과가 나오게 됨
            # break문을 통해 겹치는 단어는 표시 X
            break

# 결과 출력
print(result)