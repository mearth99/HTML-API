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
# docker build -t html_img .
# docker run --name html-con -v "$(pwd):/usr/src/app" -p 5000:5000 html-img