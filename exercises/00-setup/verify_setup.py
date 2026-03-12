"""
Claude Code Workshop - Setup Verification Script
Run this to check that everything is installed and configured correctly.

Usage:
    python3 exercises/00-setup/verify_setup.py
"""

import subprocess
import os
import sys
import shutil


def check(name, passed, message=""):
    status = "PASS" if passed else "FAIL"
    icon = "[OK]" if passed else "[!!]"
    print(f"  {icon} {name}")
    if message and not passed:
        print(f"      -> {message}")
    return passed


def main():
    print("\n" + "=" * 50)
    print("  Claude Code Workshop - Setup Verification")
    print("=" * 50 + "\n")

    results = []

    # Check Python
    print("Checking Python...")
    py_version = sys.version_info
    results.append(check(
        f"Python installed (version {py_version.major}.{py_version.minor}.{py_version.micro})",
        py_version.major == 3 and py_version.minor >= 8,
        "Python 3.8 or higher is required."
    ))

    # Check Git
    print("\nChecking Git...")
    git_path = shutil.which("git")
    if git_path:
        try:
            result = subprocess.run(["git", "--version"], capture_output=True, text=True)
            git_version = result.stdout.strip()
            results.append(check(f"Git installed ({git_version})", True))
        except Exception:
            results.append(check("Git installed", False, "Git found but couldn't get version."))
    else:
        results.append(check(
            "Git installed",
            False,
            "Git is not installed. See Exercise 0 instructions."
        ))

    # Check Git config
    try:
        name_result = subprocess.run(
            ["git", "config", "--global", "user.name"],
            capture_output=True, text=True
        )
        git_name = name_result.stdout.strip()
        results.append(check(
            f"Git user.name configured ({git_name})",
            bool(git_name),
            'Run: git config --global user.name "Your Name"'
        ))
    except Exception:
        results.append(check("Git user.name configured", False, "Could not check git config."))

    # Check VS Code (optional - might not be detectable from terminal)
    print("\nChecking VS Code...")
    code_path = shutil.which("code")
    results.append(check(
        "VS Code 'code' command available",
        code_path is not None,
        "Not critical — VS Code may still be installed but the 'code' command isn't in PATH."
    ))

    # Check OpenRouter environment variables
    print("\nChecking OpenRouter configuration...")

    base_url = os.environ.get("ANTHROPIC_BASE_URL", "")
    results.append(check(
        "ANTHROPIC_BASE_URL is set",
        "openrouter" in base_url.lower(),
        f'Expected URL containing "openrouter", got: "{base_url or "(not set)"}"'
    ))

    auth_token = os.environ.get("ANTHROPIC_AUTH_TOKEN", "")
    results.append(check(
        "ANTHROPIC_AUTH_TOKEN is set",
        auth_token.startswith("sk-or-"),
        "Should start with 'sk-or-'. Check your OpenRouter API key."
    ))

    # ANTHROPIC_API_KEY must be explicitly empty
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    results.append(check(
        "ANTHROPIC_API_KEY is set to empty string",
        api_key == "",
        'Must be explicitly set to "" (empty string). '
        'Run: export ANTHROPIC_API_KEY=""'
    ))

    model = os.environ.get("ANTHROPIC_DEFAULT_SONNET_MODEL", "")
    results.append(check(
        f"Default model configured ({model or 'not set'})",
        bool(model),
        "Set ANTHROPIC_DEFAULT_SONNET_MODEL to a free OpenRouter model."
    ))

    # Summary
    print("\n" + "=" * 50)
    passed = sum(results)
    total = len(results)
    print(f"\n  Results: {passed}/{total} checks passed\n")

    if all(results):
        print("  All checks passed! You're ready for the workshop.")
    else:
        failed = total - passed
        print(f"  {failed} check(s) need attention — see the [!!] items above.")
        print("  Don't panic! Your instructor can help at the start of class.")

    print()


if __name__ == "__main__":
    main()
