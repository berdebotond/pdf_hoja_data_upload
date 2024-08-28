import fitz  # PyMuPDF
from supabase import create_client, Client
import os
from country_name_translator import translate_countries_from_en_es

# Initialize Supabase client
url: str = os.environ.get("SUPABASE_URL", "https://hetrvidiwvkrxaqeozgc.supabase.co")
key: str = os.environ.get("SUPABASE_KEY",
                          "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhldHJ2aWRpd3ZrcnhhcWVvemdjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTM1NTE5NTUsImV4cCI6MjAyOTEyNzk1NX0.dpUKNQ65qsZaiRlrKoj9jiWhvdzhuFFxBP1ENGd_jGs")

supabase: Client = create_client(url, key)

nie_tie_selection = {
    "family_status": ["Button1", "Button2", "Button3", "Button4", "Button5"],
    "gender": ["Button6", "Button7"],
    "consent_communication_electronically": ["Button8"],
    "apply_digital_certificate": ["Button9"],
    "no_consent_data_consultation": ["Button10"]
}

nie_tie_pdf_fields_data = {
    "name": "field1",
    "surname": "field2",
    "city_of_birth": "field3",
    "country_of_birth": "field4",
    "full_name_of_father": "field5",
    "full_name_of_mother": "field6",
    "spain_address": "field7",
    "house_name": "field8",
    "apt_number": "field9",
    "city": "field10",
    "zip_code": "field11",
    "province": "field12",
    "legal_representative_name": "field13",
    "legal_representative_id": "field14",
    "legal_representative_relation": "field15",
}

initial_data_selection = {
    "mobile_phone": ["field9", "field10"],
    "desired_service": ["Button3", "Button4", "Button5", "Button6", "Button7", "Button8"],
    "appointment_location": ["Button9", "Button10"],
    "referral_source": ["Button11", "Button12", "Button13", "Button14", "Button15", "Button16"]
}

parse_initial_data_fields = {
    "first_names": "field1",
    "surnames": "field2",
    "birth_date": "field3",
    "nationality": "field4",
    "additional_nationality": "field5",
    "passport_number": "field6",
    "id_number": "field7",
    "nie": "field8",
    "email": "field11",
    "city": "field12",
    "province": "Choice19",
    "not_available_appointments": "field13",
    "appointment_deadline": "field14",
    "desired_service": "field16",
    "comments": "field17"

}

empadron_data = {
    "street_name": "field_0",
    "type": "field_1",
    "zip_code": "field_2",
    "municipality": "field_3",
    "number": "field_4",
    "letter": "field_5",
    "block": "field_6",
    "gate": "field_7",
    "stairs": "field_8",
    "floor": "field_9",
    "door": "field_10",
    "voluntary_statement": "field_11",
    "inhabitants_not_removed": "field_15",
    "rent_contract": "field_16",
    "landlord_name": "field_20",
    "landlord_id_dni_nie": "field_21",
    "first_name_1": "field13",
    "surname_1": "field14",
    "nie_1": "field15",
    "male_1": "field_53",
    "female_1": "field_54",
    "city_of_birth_1": "field_55",
    "country_of_birth_1": "field_56",
    "highest_education_1": "field_57",
    "reason_1": "field_75",
    "birth_newborns_1": "field_76",
    "moved_within_spain_1": "field_77",
    "change_personal_data_1": "field_78",
    "vote_municipal_level_1": "field_79",
    "change_europe_voting_right_1": "field_80",
    "first_name_2": "field20",
    "surname_2": "field_64",
    "nie_2": "field_71",
    "male_2": "field_67",
    "female_2": "field_68",
    "city_of_birth_2": "field_55",
    "country_of_birth_2": "field_56",
    "highest_education_2": "field_86",
    "reason_2": "field_81",
    "birth_newborns_2": "field_77",
    "moved_within_spain_2": "field_78",
    "change_personal_data_2": "field_79",
    "vote_municipal_level_2": "field_80",
    "change_europe_voting_right_2": "field_81",
    "first_name_3": "field_64",
    "surname_3": "field_65",
    "nie_3": "field_72",
    "male_3": "field_67",
    "female_3": "field_68",
    "city_of_birth_3": "field_55",
    "country_of_birth_3": "field_56",
    "highest_education_3": "field_87",
    "reason_3": "field_82",
    "birth_newborns_3": "field_78",
    "moved_within_spain_3": "field_79",
    "change_personal_data_3": "field_80",
    "vote_municipal_level_3": "field_81",
    "change_europe_voting_right_3": "field_82",
    "first_name_4": "field_65",
    "surname_4": "field_66",
    "nie_4": "field_73",
    "male_4": "field_67",
    "female_4": "field_68",
    "city_of_birth_4": "field_55",
    "country_of_birth_4": "field_56",
    "highest_education_4": "field_88",
    "reason_4": "field_83",
    "birth_newborns_4": "field_79",
    "moved_within_spain_4": "field_80",
    "change_personal_data_4": "field_81",
    "vote_municipal_level_4": "field_82",
    "change_europe_voting_right_4": "field_83",
    "first_name_5": "field_66",
    "surname_5": "field_67",
    "nie_5": "field_74",
    "male_5": "field_67",
    "female_5": "field_68",
    "city_of_birth_5": "field_55",
    "country_of_birth_5": "field_56",
    "highest_education_5": "field_89",
    "reason_5": "field_84",
    "birth_newborns_5": "field_80",
    "moved_within_spain_5": "field_81",
    "change_personal_data_5": "field_82",
    "vote_municipal_level_5": "field_83",
    "change_europe_voting_right_5": "field_84"
}


def read_pdf_custom_id(pdf_path):
    doc = fitz.open(pdf_path)
    custom_id = None
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        for annot in page.annots():

            text = annot.info["content"]
            if text.startswith("ID: "):
                custom_id = text[4:]
                break
        if custom_id:
            break
    print(f"Custom ID: {custom_id}")
    return custom_id


def upload_to_supabase(data, table_name):
    response = supabase.table(table_name).insert(data).execute()
    return response


def process_widget_nie_tie(data, widget: fitz.Widget) -> dict:
    #print(f"Processing widget: {widget.field_name}, Value: {widget.field_value}, States: {widget.button_states()}")
    if "field" in widget.field_name:
        for key, value in nie_tie_pdf_fields_data.items():
            if widget.field_name == value:
                translataion_try = translate_countries_from_en_es(widget.field_value)
                if translataion_try != widget.field_value:
                    data[key] = translataion_try
                else:
                    data[key] = widget.field_value
    elif "Button" in widget.field_name:
        if widget.field_value == "No":  # checking off means Off state, No mena it checked
            if widget.field_name == "Button1":
                data["family_status"] = "single"
            elif widget.field_name == "Button2":
                data["family_status"] = "married"
            elif widget.field_name == "Button3":
                data["family_status"] = "widowed"
            elif widget.field_name == "Button4":
                data["family_status"] = "divorced"
            elif widget.field_name == "Button5":
                data["family_status"] = "separated"
    #print(f"Processing widget: {widget.field_name}, Value: {widget.field_value}, States: {widget.button_states()}")
    if "field" in widget.field_name:
        for key, value in nie_tie_pdf_fields_data.items():
            if widget.field_name == value:
                translataion_try = translate_countries_from_en_es(widget.field_value)
                if translataion_try != widget.field_value:
                    data[key] = translataion_try
                else:
                    data[key] = widget.field_value
    elif "Button" in widget.field_name:
        #print(widget.is_signed, widget.field_value, widget.button_states(), widget.border_dashes, widget.field_label, widget.field_type, widget.field_flags)

        if widget.field_value == "No":  # checking off means Off state, No mena it checked
            if widget.field_name == "Button1":
                data["family_status"] = "single"
            elif widget.field_name == "Button2":
                data["family_status"] = "married"
            elif widget.field_name == "Button3":
                data["family_status"] = "widowed"
            elif widget.field_name == "Button4":
                data["family_status"] = "divorced"
            elif widget.field_name == "Button5":
                data["family_status"] = "separated"
            elif widget.field_name == "Button6":
                data["gender"] = "male"
            elif widget.field_name == "Button7":
                data["gender"] = "female"
            elif widget.field_name == "Button8":
                data["consent_communication_electronically"] = True
            elif widget.field_name == "Button9":
                data["apply_digital_certificate"] = True
            elif widget.field_name == "Button10":
                data["no_consent_data_consultation"] = True
    elif "Choice" in widget.field_name:
        if widget.field_name == "Choice19":
            data["province"] = widget.field_value
        else:
            data[widget.field_name] = widget.field_value
    return data


def process_widget_initial_data(data, widget: fitz.Widget) -> dict:
    #print(f"Processing widget: {widget.field_name}, Value: {widget.field_value}, States: {widget.button_states()}")
    if "field" in widget.field_name:
        if widget.field_name in ["field9", "field10"]:
            if "mobile_phone" not in data:
                data["mobile_phone"] = ""
            data["mobile_phone"] += widget.field_value
        else:
            for key, value in parse_initial_data_fields.items():
                if widget.field_name == value and widget.field_value != "":
                    translataion_try = translate_countries_from_en_es(widget.field_value)
                    if translataion_try != widget.field_value:
                        data[key] = translataion_try
                    else:
                        data[key] = widget.field_value
    elif "Button" in widget.field_name:
        if widget.field_value == "No":  # checking off means Off state, No mena it checked

            if "Button3" in widget.field_name:
                data["desired_service"] = "White NIE"
            elif "Button4" in widget.field_name:
                data["desired_service"] = "Green NIE"
            elif "Button5" in widget.field_name:
                data["desired_service"] = "TIE"
            elif "Button6" in widget.field_name:
                data["desired_service"] = "Empadronamiento & Travel Discount"
            elif "Button7" in widget.field_name:
                data["desired_service"] = "Autónomo"
            elif "Button8" in widget.field_name:
                data["desired_service"] = "Other"
            elif widget.field_name == "Button9":
                data["appointment_location"] = "Nearby cities"
            elif widget.field_name == "Button10":
                data["appointment_location"] = "My city"
            elif widget.field_name == "Button11":
                data["referral_source"] = "Slack LUP Nelly"
            elif widget.field_name == "Button12":
                data["referral_source"] = "Friend"
            elif widget.field_name == "Button13":
                data["referral_source"] = "Facebook"
            elif widget.field_name == "Button14":
                data["referral_source"] = "Website"
            elif widget.field_name == "Button15":
                data["referral_source"] = "Flyer"
            elif widget.field_name == "Button16":
                data["referral_source"] = "Poster"
    elif "Choice" in widget.field_name:
        if widget.field_name == "Choice19":
            data["province"] = widget.field_value
        else:
            data[widget.field_name] = widget.field_value
    return data


def check_pdf_type(doc):
    first_page_text = doc.load_page(0).get_text()
    #print(f"First page text: {first_page_text}")
    if "Data Sheet for NIE/TIE" in first_page_text:
        return "data_sheet_nie_tie"
    elif "Initial Data for Request of Service" in first_page_text:
        return "initial_data_request"
    return None


# Helper function to determine if a value should be a boolean
def convert_to_boolean(value):
    if value.lower() in ['yes', 'true', '1']:
        return True
    elif value.lower() in ['no', 'false', '0']:
        return False
    return value


# Extract data from PD

def process_widget_empadronamiento(data, widget):
    pass


def process_pdfs(folder_path):
    bool_index = 1
    string_index = 1
    choice_index = 1
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_id = read_pdf_custom_id(os.path.join(folder_path, filename))
            if pdf_id:
                print(f"PDF ID: {pdf_id}")
            pdf_path = os.path.join(folder_path, filename)
            doc = fitz.open(pdf_path)
            pdf_type = check_pdf_type(doc)
            data = {}
            for page in doc:
                for widget in page.widgets():
                    if widget.field_type == 2:
                        widget.field_name = "Button" + str(bool_index)
                        string_index += 1
                    elif widget.field_type == 7:
                        widget.field_name = "field" + str(string_index)

                    if pdf_type == "data_sheet_nie_tie":
                        data = process_widget_nie_tie(data, widget)
                    elif pdf_type == "initial_data_request":
                        data = process_widget_initial_data(data, widget)
                    elif pdf_type == "empadronamiento":
                        data = process_widget_empadronamiento(data, widget)
            print(data)

            if pdf_type:
                #print(f"Data for {filename}: {data}")  # Print data for debugging
                upload_to_supabase(data, pdf_type)
                print(f"Uploaded {pdf_type} to Supabase")


# Run the process
process_pdfs('/Users/botondberde/research/pdf_fix_jonna/pdfs_to_db/input_pdfs/')
