class BallotManager:
    def __init__(self):
        self.ballots = {}

    def create_ballot(self, election_id, candidates):
        self.ballots[election_id] = candidates
        return f"Ballot for election {election_id} created with candidates {candidates}."