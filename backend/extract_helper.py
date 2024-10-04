import re



def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(0)# extract the whole session-id
        return extracted_string

    return ""


# convert from {'couscous':2 ,'mint tea':1}to 2 Couscous 1 mint tea

def food_dict_to_str(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result
