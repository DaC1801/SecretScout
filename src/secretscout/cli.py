from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from .commands import cmd_baseline, cmd_init, cmd_scan, cmd_stats
from .reporting import Format
from .rules_cmd import list_rules, show_rule

app = typer.Typer(
    add_completion=False,
    help="SecretScout: defensive secret scanner for repos and folders.",
)

# ---- Reusable annotations (Ruff B008-safe) ----

PathArg = Annotated[
    Path,
    typer.Argument(exists=True, file_okay=False, dir_okay=True),
]

FormatOpt = Annotated[
    Format,
    typer.Option("--format", help="table|minimal|json|sarif|html"),
]

OutputOpt = Annotated[
    Path | None,
    typer.Option("--output", "-o", help="Write report to file (else stdout)."),
]

FailOnOpt = Annotated[
    str,
    typer.Option("--fail-on", help="Exit 1 if findings severity >= this."),
]

BaselineOpt = Annotated[
    Path | None,
    typer.Option("--baseline", help="Baseline JSON file to ignore known findings."),
]

StagedOpt = Annotated[
    bool,
    typer.Option("--staged", help="Scan staged changes (git index)."),
]

TrackedOpt = Annotated[
    bool,
    typer.Option("--tracked", help="Scan only git tracked files."),
]

AllFilesOpt = Annotated[
    bool,
    typer.Option("--all", help="Scan all files under PATH (ignores git)."),
]

ExcludeOpt = Annotated[
    list[str] | None,
    typer.Option("--exclude", help="Extra exclude glob patterns (repeatable)."),
]

NoCacheOpt = Annotated[
    bool,
    typer.Option("--no-cache", help="Disable cache."),
]

MaxFindingsOpt = Annotated[
    int | None,
    typer.Option("--max-findings", help="Limit output findings."),
]

# ---- Commands ----


@app.command()
def scan(
    path: PathArg = Path("."),
    format: FormatOpt = "table",
    output: OutputOpt = None,
    fail_on: FailOnOpt = "high",
    baseline: BaselineOpt = None,
    staged: StagedOpt = False,
    tracked: TrackedOpt = False,
    all_files: AllFilesOpt = False,
    exclude: ExcludeOpt = None,
    no_cache: NoCacheOpt = False,
    max_findings: MaxFindingsOpt = None,
) -> None:
    """Scan a path for potential secrets."""
    code = cmd_scan(
        path=path,
        fmt=format,
        output=output,
        fail_on=fail_on,
        baseline=baseline,
        staged=staged,
        tracked=tracked,
        all_files=all_files,
        exclude=exclude or [],
        no_cache=no_cache,
        max_findings=max_findings,
    )
    raise typer.Exit(code=code)


@app.command()
def init(path: PathArg = Path(".")) -> None:
    """Generate default config and ignore files."""
    raise typer.Exit(code=cmd_init(path))


@app.command()
def fix(path: PathArg = Path(".")) -> None:
    """Alias for init (kept for convenience)."""
    raise typer.Exit(code=cmd_init(path))


@app.command()
def baseline(
    path: PathArg = Path("."),
    output: Annotated[
        Path,
        typer.Option("--output", "-o", help="Baseline output file."),
    ] = Path(".secretscout.baseline.json"),
    tracked: Annotated[
        bool,
        typer.Option("--tracked/--all", help="By default, baseline git-tracked files."),
    ] = True,
) -> None:
    """Create a baseline file to ignore known findings."""
    raise typer.Exit(code=cmd_baseline(path, output, tracked))


@app.command()
def stats(
    path: PathArg = Path("."),
    staged: StagedOpt = False,
    tracked: TrackedOpt = False,
    all_files: AllFilesOpt = False,
    baseline: BaselineOpt = None,
) -> None:
    """Show a summary of findings."""
    raise typer.Exit(
        code=cmd_stats(
            path,
            staged=staged,
            tracked=tracked,
            all_files=all_files,
            baseline=baseline,
        )
    )


# ---- Rules subcommands ----

rules_app = typer.Typer(help="Manage and inspect rules.")
app.add_typer(rules_app, name="rules")


@rules_app.command("list")
def rules_list() -> None:
    """List available rules."""
    list_rules()


@rules_app.command("show")
def rules_show(
    rule_id: Annotated[str, typer.Argument(help="Rule id (e.g. github-token).")],
) -> None:
    """Show details for a single rule."""
    show_rule(rule_id)
