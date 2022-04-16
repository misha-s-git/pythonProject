import json


def get_candidates(path):
    with open(path, "r", encoding="UTF-8") as file:
        return json.load(file)


def format_candidates(candidates_list):
    result = "<pre>"
    for candidate in candidates_list:
        result += (
            f"Имя кандидата - {candidate['name']}\n"
            f"Позиция кандидата - {candidate['position']}\n"
            f"Навыки через запятую - {candidate['skills']}\n"
        )

        result += "\n<pre>"

    return result

def get_candidates_by_id(candidates_list, candidate_id):
    candidate_id = int(candidate_id)
    for candidate in candidates_list:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_skill(candidates_list, candidates_skill):
    result = []

    for candidate in candidates_list:
        candidates_skills = candidate['skills'].lower().split(', ')
        if candidates_skill in candidates_skills:
            result.append(candidate)

    return result

