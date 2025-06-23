# 사내 매거진 댓글 시스템 설정 가이드

## 📋 개요

이 가이드는 사내 매거진 웹사이트의 댓글 시스템을 Google Apps Script와 Google Sheets를 사용하여 설정하는 방법을 설명합니다.

## 🚀 1단계: Google Sheets 설정

### 1.1 새 Google Sheets 생성

1. [Google Sheets](https://sheets.google.com)에 접속
2. 새 스프레드시트 생성
3. 스프레드시트 이름을 "사내매거진\_댓글시스템"으로 변경

### 1.2 스프레드시트 ID 복사

1. 브라우저 주소창에서 스프레드시트 ID 복사
    - 예: `https://docs.google.com/spreadsheets/d/`**`1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms`**`/edit`
    - 굵은 부분이 스프레드시트 ID입니다.
    - **중요**: 이 ID를 복사해서 나중에 Google Apps Script에서 사용합니다.

### 1.3 스프레드시트 구조 확인

스프레드시트에 다음과 같은 열이 자동으로 생성됩니다:

-   **A열**: 댓글 ID (자동 생성)
-   **B열**: 작성자 이름
-   **C열**: 댓글 내용
-   **D열**: 작성 시간
-   **E열**: 좋아요 수
-   **F열**: 익명 여부

## 🔧 2단계: Google Apps Script 설정

### 2.1 새 Apps Script 프로젝트 생성

1. [Google Apps Script](https://script.google.com)에 접속
2. "새 프로젝트" 클릭
3. 프로젝트 이름을 "사내매거진\_댓글API"로 변경

### 2.2 코드 복사

1. `google-apps-script.js` 파일의 내용을 복사
2. Apps Script 편집기에 붙여넣기
3. **중요**: `SPREADSHEET_ID` 변수를 실제 스프레드시트 ID로 변경

```javascript
const SPREADSHEET_ID = "여기에_실제_스프레드시트_ID_입력";
```

**스프레드시트 ID 찾는 방법:**

-   Google Sheets URL: `https://docs.google.com/spreadsheets/d/`**`1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms`**`/edit`
-   굵은 부분을 복사해서 `SPREADSHEET_ID`에 붙여넣기

**⚠️ 주의사항:**

-   **Google Apps Script 웹앱 URL의 ID가 아닙니다!**
-   **실제 Google Sheets의 ID여야 합니다!**
-   웹앱 URL: `https://script.google.com/macros/s/`**`AKfycbw8Ka_UYxBWkSNKxFdcKNsmgJHztIXbs-NvxeOVhBJCNU2zLMtc_OFcZU29ymb6nOXYBg`**`/exec` ← 이건 웹앱 ID
-   스프레드시트 URL: `https://docs.google.com/spreadsheets/d/`**`1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms`**`/edit` ← 이게 스프레드시트 ID

**예시:**

```javascript
const SPREADSHEET_ID = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms";
```

### 2.3 웹 앱 배포

1. "배포" → "새 배포" 클릭
2. "유형 선택" → "웹 앱" 선택
3. 설정:
    - **설명**: "사내매거진 댓글 API v1.0"
    - **실행 대상**: "나"
    - **액세스 권한**: "모든 사용자"
4. "배포" 클릭
5. 권한 승인 (필요시)
6. **웹 앱 URL 복사** (중요!)

## 🌐 3단계: HTML 파일 설정

### 3.1 API URL 업데이트

`index.html` 파일에서 다음 부분을 찾아 실제 웹 앱 URL로 변경:

```javascript
const GAS_API_URL = "YOUR_GOOGLE_APPS_SCRIPT_WEB_APP_URL"; // 이 부분을 실제 URL로 변경
```

예시:

```javascript
const GAS_API_URL =
    "https://script.google.com/macros/s/AKfycbz1234567890abcdef/exec";
```

## 🧪 4단계: 테스트

### 4.1 Apps Script 테스트

1. Apps Script 편집기에서 `testCommentSystem` 함수 실행
2. 로그에서 테스트 결과 확인

### 4.2 웹사이트 테스트

1. 웹사이트 접속
2. 댓글 작성 테스트
3. 새로고침 버튼 테스트
4. 좋아요 기능 테스트

## 📊 5단계: 데이터 관리

### 5.1 백업 설정

-   Apps Script에서 `backupComments` 함수를 수동으로 실행하거나
-   트리거를 설정하여 자동 백업 가능

### 5.2 데이터 정리

-   `cleanupOldComments` 함수로 30일 이상 된 댓글 자동 삭제
-   필요시 기간 조정 가능

## 🔒 6단계: 보안 설정

### 6.1 스프레드시트 권한

1. 스프레드시트 공유 설정 확인
2. Apps Script 프로젝트에만 접근 권한 부여

### 6.2 웹 앱 보안

1. 웹 앱 배포 설정에서 "액세스 권한" 확인
2. 필요시 특정 도메인으로 제한

## 🐛 문제 해결

### 일반적인 문제들

#### 1. CORS 오류

```
Access to fetch at '...' from origin '...' has been blocked by CORS policy
```

**해결방법**:

-   Apps Script 코드의 CORS 헤더가 올바르게 설정되었는지 확인
-   GET 방식으로 API 호출하도록 변경 (POST 대신)
-   웹앱 재배포 필요

#### 2. 스프레드시트 접근 오류

```
스프레드시트에 접근할 수 없습니다.
```

**해결방법**:

-   **스프레드시트 ID가 올바른지 확인** (가장 중요!)
-   웹앱 ID와 스프레드시트 ID를 혼동하지 마세요
-   스프레드시트 공유 설정 확인
-   Apps Script 권한 확인

#### 3. 댓글이 저장되지 않음

**해결방법**:

-   웹 앱 URL이 올바른지 확인
-   브라우저 개발자 도구에서 네트워크 오류 확인
-   Apps Script 로그에서 오류 메시지 확인

### 디버깅 방법

#### 1. Apps Script 로그 확인

1. Apps Script 편집기에서 "실행" → "실행 로그" 확인
2. 오류 메시지 및 실행 흐름 파악

#### 2. 브라우저 개발자 도구

1. F12 키로 개발자 도구 열기
2. Console 탭에서 JavaScript 오류 확인
3. Network 탭에서 API 호출 상태 확인

#### 3. 스프레드시트 직접 확인

1. 스프레드시트에서 "Comments" 시트 확인
2. 데이터가 올바르게 저장되는지 확인

## 📈 성능 최적화

### 1. 캐싱 설정

-   댓글 목록을 30초마다 자동 새로고침
-   필요시 간격 조정 가능

### 2. 데이터 제한

-   최대 4개 댓글만 표시
-   스크롤로 나머지 댓글 확인 가능

### 3. 입력 제한

-   댓글 내용: 최대 500자
-   작성자 이름: 최대 20자

## 🔄 업데이트 및 유지보수

### 1. 코드 업데이트

1. Apps Script 코드 수정 후 재배포 필요
2. 웹 앱 URL은 동일하게 유지됨

### 2. 데이터 마이그레이션

1. 기존 댓글 데이터 백업
2. 새 구조로 데이터 이전
3. 테스트 후 적용

### 3. 모니터링

-   정기적으로 Apps Script 로그 확인
-   스프레드시트 데이터 정리
-   백업 데이터 관리

## 📞 지원

문제가 발생하거나 추가 도움이 필요한 경우:

-   전략기획실 지윤환 사원에게 문의
-   이메일: jyh@eibe.co.kr

---

**마지막 업데이트**: 2025년 1월
**버전**: v1.0
