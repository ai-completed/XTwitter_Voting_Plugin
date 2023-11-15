def identify_voter(voter_id):
    voter_database = {
        '12345': {'name': 'John Doe', 'verified': True},
        '67890': {'name': 'Jane Smith', 'verified': False}
    }
    voter = voter_database.get(voter_id, None)
    if voter and voter['verified']:
        return True, f"Voter {voter['name']} verified."
    else:
        return False, "Voter not found or not verified."