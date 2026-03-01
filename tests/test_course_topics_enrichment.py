from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_course_details_includes_ba_formatted_topics():
    resp = client.get("/curriculum/course/ba101")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_cs_formatted_topics():
    resp = client.get("/curriculum/course/cs101")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "cs101"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_finance_formatted_topics():
    resp = client.get("/curriculum/course/fin101")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "fin101"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_accounting_formatted_topics():
    resp = client.get("/curriculum/course/acc101")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "acc101"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_liberal_arts_formatted_topics():
    resp = client.get("/curriculum/course/lib101")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "lib101"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_economics_intro_formatted_topics():
    resp = client.get("/curriculum/course/econ101")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "econ101"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_econometrics_formatted_topics():
    resp = client.get("/curriculum/course/econ301")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "econ301"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_calculus_formatted_topics():
    resp = client.get("/curriculum/course/math101")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "math101"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_abstract_algebra_formatted_topics():
    resp = client.get("/curriculum/course/math301")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "math301"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_physics_i_formatted_topics():
    resp = client.get("/curriculum/course/phys101")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "phys101"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_physics_ii_formatted_topics():
    resp = client.get("/curriculum/course/phys102")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "phys102"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_engineering_design_formatted_topics():
    resp = client.get("/curriculum/course/eng101")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "eng101"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_thermodynamics_formatted_topics():
    resp = client.get("/curriculum/course/eng401")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "eng401"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_without_enrichment_omits_formatted_topics():
    resp = client.get("/curriculum/course/stat101")
    # If course exists and has no enrichment, field is omitted by service design.
    # If it doesn't exist in curriculum, endpoint returns 404.
    if resp.status_code == 200:
        data = resp.json()
        assert "formatted_topics" not in data
    else:
        assert resp.status_code == 404


def test_course_details_includes_data_science_formatted_topics():
    resp = client.get("/curriculum/course/ds101")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "ds101"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_data_science_ml_formatted_topics():
    resp = client.get("/curriculum/course/ds301")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "ds301"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_psychology_formatted_topics():
    resp = client.get("/curriculum/course/psych101")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "psych101"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_social_psychology_formatted_topics():
    resp = client.get("/curriculum/course/psych401")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "psych401"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_biology_formatted_topics():
    resp = client.get("/curriculum/course/bio101")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "bio101"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_political_science_formatted_topics():
    resp = client.get("/curriculum/course/pol101")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "pol101"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_international_relations_formatted_topics():
    resp = client.get("/curriculum/course/pol201")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "pol201"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_history_formatted_topics():
    resp = client.get("/curriculum/course/hist101")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "hist101"
    assert len(data["formatted_topics"]["topics"]) >= 3


def test_course_details_includes_american_history_formatted_topics():
    resp = client.get("/curriculum/course/hist301")
    assert resp.status_code == 200
    data = resp.json()

    assert "formatted_topics" in data
    assert data["formatted_topics"]["found"] is True
    assert data["formatted_topics"]["course_id"] == "hist301"
    assert len(data["formatted_topics"]["topics"]) >= 3
