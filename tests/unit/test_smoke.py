"""Smoke tests: packages import cleanly, base models construct."""


def test_kfin_dart_imports() -> None:
    import kfin_dart

    assert kfin_dart.__version__


def test_native_extension_imports() -> None:
    import kfin_dart_rs

    assert kfin_dart_rs.version()


def test_base_models_construct() -> None:
    from kfin_dart.models import AuditOpinion, ExtractedField, SourceRef

    ref = SourceRef(page=1, extraction_method="rule", confidence=0.95)
    auditor = ExtractedField(
        value="삼일회계법인",
        source=ref,
        raw_text="삼일회계법인",
    )
    sign_date = ExtractedField(value="2025-03-15", source=ref)
    opinion = AuditOpinion(
        opinion_type="적정",
        auditor_firm=auditor,
        sign_date=sign_date,
    )
    assert opinion.opinion_type == "적정"
    assert opinion.going_concern is False
    assert opinion.kam_items == []
