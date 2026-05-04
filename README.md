# kfin-dart

> Korean DART disclosure parser for auditors and investors — XBRL-aware, audit-traceable, low-token extraction.

[한국어](#한국어) · [English](#english)

---

## 한국어

**kfin-dart**는 한국 금융감독원 DART에 공시되는 사업보고서·감사보고서·분반기검토보고서를 감사인과 투자자가 즉시 활용 가능한 구조화 데이터로 변환하는 결정론적 추출 라이브러리입니다.

### 차별점

- **Korean DART 양식 특화** — 금감원 표준 양식 사전 지식 주입
- **XBRL-aware** — 재무제표는 XBRL 우선, PDF는 검증·텍스트용 이중 트랙
- **Audit-traceable** — 추출 결과의 원문 페이지·좌표 역추적 가능
- **Low-token** — 결정론적 처리 95% / LLM 폴백 5%, 비용 사실상 상수
- **듀얼 페르소나** — 동일 추출 코어에서 감사인·투자자 view 분기

### 처리 모델

| 레이어 | 역할 | 기술 | LLM |
| --- | --- | --- | --- |
| L1 | 보고서 타입·연도 식별 | 룰 기반 (Rust) | 0 |
| L2 | 목차·페이지 경계 추출 | 정규식 + 위치 (Rust) | 0 |
| L3 | 섹션별 구조화 | pdfplumber / lxml / Rust | 0 |
| L4 | 변형·자유서술 해석 | Claude | 최소 |

### 상태

Pre-alpha. M0 인프라 셋업 단계. Phase A 스코프: 사업보고서 + 감사보고서 + 분반기검토.

### 라이선스

AGPL-3.0-only. 자세한 내용은 [LICENSE](LICENSE) 참조.

---

## English

**kfin-dart** turns Korea DART filings (annual reports, audit reports, quarterly reviews) into structured data ready for auditors and investors. Deterministic-first, XBRL-aware, with full provenance back to the source PDF.

### Why this exists

- **Korean-form-specific** — encodes FSC standard layouts as prior knowledge
- **XBRL-aware** — financials come from XBRL first; PDFs are used for cross-validation and narrative
- **Audit-traceable** — every extracted value carries the page and bbox it came from
- **Low-token** — ~95% deterministic, ~5% LLM fallback; cost is essentially flat per filing
- **Dual persona** — one extraction core, two views (auditor / investor)

### Processing model

| Layer | Role | Tech | LLM |
| --- | --- | --- | --- |
| L1 | Classify report type and year | Rules (Rust) | 0 |
| L2 | Section / page boundary detection | Regex + layout (Rust) | 0 |
| L3 | Section-specific structuring | pdfplumber / lxml / Rust | 0 |
| L4 | Variant and free-form parsing | Claude | minimal |

### Status

Pre-alpha. Setting up M0 infrastructure. Phase A scope: annual reports, audit reports, quarterly reviews.

### License

AGPL-3.0-only. See [LICENSE](LICENSE).
