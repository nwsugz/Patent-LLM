# 민법
import PyPDF2
import json
import os
import re

def clean_text(text):
    # 페이지 번호, 법제처, 국가법령정보센터, 민법 등 불필요한 텍스트 제거
    text = re.sub(r'법제처\s+\d+\s+국가법령정보센터', '', text)
    text = re.sub(r'민법\s*', '', text)
    text = re.sub(r'page_\d+', '', text)
    
    # 연속된 공백을 하나의 공백으로 대체
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def pdf_to_json(pdf_path):
    # PDF 파일 경로에서 파일 이름과 디렉토리 추출
    pdf_dir = os.path.dirname(pdf_path)
    pdf_filename = os.path.basename(pdf_path)
    json_filename = os.path.splitext(pdf_filename)[0] + '.json'
    json_path = os.path.join(pdf_dir, json_filename)

    # PDF 파일 열기
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # 모든 페이지의 텍스트 추출 및 정제
        full_text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            full_text += clean_text(page_text) + " "
        
        # 정제된 텍스트를 딕셔너리에 저장
        text_data = {"civil_law": full_text.strip()}
        
        # JSON 파일로 저장
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(text_data, json_file, ensure_ascii=False, indent=4)

    print(f"PDF 내용이 {json_path}에 JSON 형식으로 저장되었습니다.")

# PDF 파일 경로
pdf_path = '/home/user/hjkim/crawling/pdf/민법.pdf'

# 함수 호출
pdf_to_json(pdf_path)