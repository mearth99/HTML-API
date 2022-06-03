# HTML-API

API를 이용해 입력한 내용을 반드시 포함하는 댓글을 만들어보았다.

# using API URL 
    url = "https://master-gpt2-everytime-fpem123.endpoint.ainize.ai/everytime/fix-length"

# ex) 
    data = {
            "text": "안녕", 
            "category": "숭실대 에타",
            "length": 10
        }
# 사용 명령어
    docker build -t html_img .
    docker run --name html-con -v "$(pwd):/usr/src/app" -p 5000:5000 html-img
    
# 결과 이미지
    <img width="478" alt="html1" src="https://user-images.githubusercontent.com/90100440/171867524-5f158e6f-a1b9-4e6a-aa22-6b30494c6311.PNG">
    <img width="622" alt="html2" src="https://user-images.githubusercontent.com/90100440/171867586-223b7d3e-781a-4004-a6eb-883ec6c42424.PNG">
