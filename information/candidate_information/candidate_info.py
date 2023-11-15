def get_candidate_info(candidate_id):
    candidate_data = {
        '1': {'name': 'Candidate One', 'policies': 'Policy 1, Policy 2'},
        '2': {'name': 'Candidate Two', 'policies': 'Policy A, Policy B'}
    }
    return candidate_data.get(candidate_id, "Candidate information not found.")