def is_valid_state(state):
    return True


def get_candidates(state):
    return []


def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # return - if we only want one solution

    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)


def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions
