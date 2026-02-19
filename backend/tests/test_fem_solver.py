from backend.fem.solver import solve_stub


def test_solve_stub_returns_converged_result() -> None:
    result = solve_stub(dof_count=8)
    assert result.converged is True
    assert result.dof_count == 8
