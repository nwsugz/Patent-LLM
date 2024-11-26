import json
import os

def merge_json_files(directory_path):
    merged_data = {}
    
    # 디렉토리 내의 모든 파일을 확인
    for filename in os.listdir(directory_path):
        if filename.endswith('.json') and filename != 'law.json':
            file_path = os.path.join(directory_path, filename)
            
            # JSON 파일 읽기
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            # 파일 이름에서 확장자 제거
            law_name = os.path.splitext(filename)[0]
            
            # 병합된 데이터에 추가
            # 파일 내용 전체를 그대로 병합
            merged_data[law_name] = data[law_name]
    
    # 병합된 데이터를 새로운 JSON 파일로 저장
    output_path = os.path.join(directory_path, 'all_law.json')
    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(merged_data, output_file, ensure_ascii=False, indent=4)
    
    print(f"모든 JSON 파일이 {output_path}에 병합되었습니다.")

# 실행
directory_path = '/home/user/hjkim/crawling'
merge_json_files(directory_path)