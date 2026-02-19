from dataclasses import dataclass


@dataclass
class FEMResult:
    dof_count: int
    converged: bool


def solve_stub(dof_count: int = 4) -> FEMResult:
    """Simple placeholder FEM solver for scaffolding and tests."""
    return FEMResult(dof_count=dof_count, converged=dof_count > 0)
