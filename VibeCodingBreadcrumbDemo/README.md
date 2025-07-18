# VibeCodingBreadcrumbDemo

"Breadcrumb Protocol" 기반의 협업 워크플로우를 연구하는 샘플 프로젝트입니다.

## 목표
- 에이전트와 사용자의 대화 흐름을 단계별로 기록하는 "Breadcrumb" 방식 구현
- 프로젝트 진행 상황을 명확하게 추적할 수 있는 구조 제시

## 향후 계획
1. 기본적인 브레드크럼 저장 포맷 설계
2. 간단한 예제 스크립트와 함께 데모 구현
3. 다른 바이브 코딩 시나리오와의 연동 가능성 탐색

## 초기 기획안: FE/BE 구조

```mermaid
sequenceDiagram
    participant FE as Frontend
    participant API as FastAPI Backend
    participant Memory as In-Memory Store
    FE->>API: POST /breadcrumbs
    API->>Memory: Save breadcrumb
    FE->>API: GET /breadcrumbs
    API->>Memory: Retrieve list
    Memory-->>API: List
    API-->>FE: JSON list
```

### FE (프론트엔드)
- 대화 흐름을 시각적으로 확인할 수 있는 타임라인 형태의 UI 설계
- 사용자 입력 창과 브레드크럼 히스토리 화면을 중심으로 페이지를 구성
- REST API 를 통해 브레드크럼 데이터를 가져오고, 새 대화가 생성될 때마다 업데이트

### BE (백엔드)
- FastAPI 혹은 Django REST Framework 기반으로 API 서버를 구성
- 주요 엔티티: `Breadcrumb` (대화 단계, 내용, 타임스탬프 등을 저장)
- 엔드포인트 예시
  - `POST /breadcrumbs/` : 새로운 브레드크럼 생성
  - `GET /breadcrumbs/{conversation_id}` : 특정 대화의 히스토리 조회
- 초기 단계에서는 간단한 파일 혹은 인메모리 저장소를 사용하고, 추후 데이터베이스 연동을 검토


## Getting Started

### Backend
1. Install dependencies: `pip install -r backend/requirements.txt`
2. Run the server: `./backend/run.sh`

### Frontend
1. Install Node dependencies: `npm install` inside `frontend`
2. Start development server: `npm start`
