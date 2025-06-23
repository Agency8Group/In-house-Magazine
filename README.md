# 🏢 In-House Magazine | 사내 매거진

> **실시간 사내 소식, 프로젝트, 조직도, 팀 스케쥴러를 한눈에 확인하는 사내 매거진 플랫폼**

![EIBE Logo](./img/eibe.jpg)

## 📋 목차

-   [프로젝트 소개](#프로젝트-소개)
-   [주요 기능](#주요-기능)
-   [기술 스택](#기술-스택)
-   [실행 방법](#실행-방법)
-   [프로젝트 구조](#프로젝트-구조)
-   [유지보수 가이드](#유지보수-가이드)
-   [문의사항](#문의사항)

## 🎯 프로젝트 소개

EIBE 사내 매거진은 직원들이 회사의 최신 소식, 프로젝트 진행상황, 조직도, 팀 스케쥴러 등을 실시간으로 확인할 수 있는 웹 플랫폼입니다.

### 🌟 특징

-   **실시간 업데이트**: 최신 사내 소식과 프로젝트 정보 제공
-   **반응형 디자인**: 모바일, 태블릿, 데스크톱 모든 기기에서 최적화
-   **다크모드 지원**: 사용자 선호도에 따른 테마 전환
-   **직관적 UI/UX**: 사용하기 쉬운 인터페이스
-   **실시간 스케쥴러**: 팀 일정 실시간 모니터링

## 🚀 주요 기능

### 📰 지금 살펴볼 포인트

-   사내 주요 공지사항
-   신규 입사자 소개
-   정직원 발령 등 인사 정보

### 📸 포토부스

-   회사 행사 및 프로젝트 사진 갤러리
-   Swiper 캐러셀로 구성된 이미지 슬라이더
-   호버 효과와 애니메이션

### 📅 팀 스케쥴러

-   실시간 팀 일정 모니터링
-   iframe으로 외부 스케쥴러 연동
-   자동 업데이트 기능

### 💡 인사이트

-   **AI 상담포털**: 드리미 AI 상담 서비스
-   **피드백박스**: 익명 건의게시판
-   **오피스 테트리스**: 사내 게임 서비스

### 🏗️ 조직도

-   실시간 조직도 모니터링
-   iframe으로 외부 조직도 연동
-   자동 업데이트 기능

### 📄 기업소개서

-   2025 아이베 기업 소개서 PDF 뷰어
-   실시간 문서 확인

### 🤖 FAQ 챗봇

-   자주 묻는 질문 답변
-   실시간 검색 기능
-   키워드 기반 필터링

## 🛠️ 기술 스택

### Frontend

-   **HTML5**: 시맨틱 마크업
-   **CSS3**:
    -   Tailwind CSS (유틸리티 퍼스트 CSS 프레임워크)
    -   커스텀 애니메이션 및 키프레임
    -   반응형 디자인
-   **JavaScript (ES6+)**:
    -   바닐라 JavaScript
    -   모듈화된 코드 구조
    -   이벤트 핸들링

### 외부 라이브러리

-   **Swiper.js**: 이미지 캐러셀
-   **DotLottie**: Lottie 애니메이션 플레이어
-   **Google Fonts**: Inter, Noto Sans KR 폰트

### 호스팅 & 배포

-   **GitHub Pages**: 정적 웹사이트 호스팅
-   **CDN**: 외부 라이브러리 로드

## 🚀 실행 방법

### 1. 로컬 실행

```bash
# 프로젝트 클론
git clone https://github.com/your-username/In-house-Magazine.git

# 프로젝트 폴더로 이동
cd In-house-Magazine

# 로컬 서버 실행 (Python 사용)
python -m http.server 8000

# 또는 Node.js 사용
npx serve .

# 브라우저에서 접속
# http://localhost:8000
```

### 2. GitHub Pages 배포

```bash
# GitHub Pages 설정
# 1. GitHub 저장소 Settings > Pages
# 2. Source를 'Deploy from a branch'로 설정
# 3. Branch를 'main'으로 설정
# 4. Save 클릭
```

## 📁 프로젝트 구조

```
In-house-Magazine/
├── index.html              # 메인 HTML 파일
├── README.md              # 프로젝트 문서
├── img/                   # 이미지 파일들
│   └── eibe.jpg          # 회사 로고 (favicon)
├── pdf/                   # PDF 문서들
│   └── 2025 아이베 기업 소개서.pdf
├── photobooth/           # 포토부스 이미지들
│   ├── 대표님스튜디오 프로필 촬영.jpg
│   ├── 드리미 라이브방송.jpg
│   └── 드리미 본사회의.jpg
└── .gitignore            # Git 무시 파일
```

## 🔧 유지보수 가이드

### 📝 콘텐츠 업데이트

#### 1. 지금 살펴볼 포인트 수정

```html
<!-- index.html의 해당 섹션에서 수정 -->
<section id="issue" class="fade-section">
    <!-- 카드 내용 수정 -->
</section>
```

#### 2. 포토부스 이미지 추가

1. `photobooth/` 폴더에 새 이미지 추가
2. `index.html`의 Swiper 섹션에 새 슬라이드 추가:

```html
<div class="swiper-slide">
    <div class="relative group overflow-hidden rounded-2xl...">
        <img src="./photobooth/새이미지.jpg" alt="설명" />
        <!-- 오버레이 내용 -->
    </div>
</div>
```

#### 3. 인사이트 링크 수정

```html
<!-- index.html의 인사이트 섹션에서 링크 수정 -->
<a href="새로운URL" target="_blank" class="...">
    <!-- 카드 내용 -->
</a>
```

### 🎨 스타일 수정

#### 1. 색상 테마 변경

```css
/* index.html의 Tailwind 설정에서 수정 */
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: "#새로운색상코드",
                accent: "#새로운색상코드",
                // ...
            }
        }
    }
}
```

#### 2. 애니메이션 수정

```css
/* index.html의 <style> 태그 내에서 수정 */
@keyframes 새로운애니메이션 {
    /* 애니메이션 정의 */
}
```

### 🔗 외부 서비스 연동

#### 1. 팀 스케쥴러 URL 변경

```html
<!-- index.html에서 iframe src 수정 -->
<iframe src="새로운스케쥴러URL" title="조직도 실시간 모니터링"></iframe>
```

#### 2. 조직도 URL 변경

```html
<!-- index.html에서 iframe src 수정 -->
<iframe src="새로운조직도URL" title="조직도 실시간 모니터링"></iframe>
```

### 📱 반응형 디자인 수정

```css
/* 모바일 대응 */
@media (max-width: 768px) {
    /* 모바일 스타일 */
}

/* 태블릿 대응 */
@media (max-width: 1024px) {
    /* 태블릿 스타일 */
}
```

### 🤖 FAQ 챗봇 수정

```javascript
// index.html의 script 태그 내에서 수정
const faqList = [
    {
        q: "새로운 질문",
        a: "새로운 답변",
    },
    // ...
];
```

## 🐛 문제 해결

### 일반적인 문제들

#### 1. 이미지가 로드되지 않는 경우

-   파일 경로 확인
-   파일명 대소문자 확인
-   파일 존재 여부 확인

#### 2. 외부 서비스가 로드되지 않는 경우

-   인터넷 연결 확인
-   URL 유효성 확인
-   CORS 정책 확인

#### 3. 애니메이션이 작동하지 않는 경우

-   브라우저 호환성 확인
-   CSS 문법 오류 확인
-   JavaScript 오류 확인

## 📞 문의사항

### 유지보수 담당자

-   **담당자**: 전략기획실 지윤환
-   **이메일**: jyh@eibe.co.kr
-   **연락처**: 사내 연락망

### 버그 리포트

버그나 개선사항이 있으시면:

1. 이슈를 상세히 기술
2. 발생 환경 (브라우저, OS 등) 명시
3. 담당자에게 직접 연락

### 기능 요청

새로운 기능 추가 요청이 있으시면:

1. 요청 기능 상세 설명
2. 기대 효과 명시
3. 우선순위 설정

---

## 📄 라이선스

© 2025 Yoonwhan Ji. All rights reserved.

---

**마지막 업데이트**: 2025년 1월
**버전**: v1.0.0
