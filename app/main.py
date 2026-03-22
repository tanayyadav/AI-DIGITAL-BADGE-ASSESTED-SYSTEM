from fastapi import FastAPI
from app.schemas.input_schemas import (
    FormInputSchema,
    FreeTextInputSchema,
    OBv3InputSchema
)
from app.services.input_parser import (
    parse_form_input,
    parse_text_input,
    parse_obv3_input
)
from app.services.normalization_service import normalize_raw_input
#from app.schemas.fact_sheet_schema import BadgeFactSheet

app = FastAPI(title="Digital Badge Classification Tool - Input Layer")


@app.get("/")
def home():
    return {"message": "FastAPI input layer is running"}


@app.post("/input/form")
def accept_form_input(data: FormInputSchema):
    parsed_data = parse_form_input(data)
    normalized_data = normalize_raw_input(parsed_data)
    return {
        "message": "Form input normalized successfully",
        "normalized_data": normalized_data
    }


@app.post("/input/text")
def accept_text_input(data: FreeTextInputSchema):
    parsed_data = parse_text_input(data)
    normalized_data = normalize_raw_input(parsed_data)
    return {
        "message": "Free-text input normalized successfully",
        "normalized_data": normalized_data
    }


@app.post("/input/obv3")
def accept_obv3_input(data: OBv3InputSchema):
    parsed_data = parse_obv3_input(data)
    normalized_data = normalize_raw_input(parsed_data)
    return {
        "message": "OBv3 JSON normalized successfully",
        "normalized_data": normalized_data
    }