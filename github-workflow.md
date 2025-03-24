# GitHub & Linear Workflow Best Practices

## Overview

This document outlines our optimized Git and PR workflow, leveraging Linear integration and GitHub Actions CI. This workflow ensures code quality, maintainability, and efficient team collaboration.

## Branch Management

### Branch Naming Convention

All branches should follow this format:
```
<type>/<linear-id>-<short-description>
```

Where:
- `<type>` is one of:
  - `feature` - New functionality
  - `bugfix` - Bug fixes
  - `hotfix` - Critical production fixes
  - `refactor` - Code improvements without behavior changes
  - `chore` - Maintenance tasks
  - `docs` - Documentation updates
- `<linear-id>` is the Linear ticket ID (e.g., AI-123)
- `<short-description>` is a brief, kebab-case description

Examples:
```
feature/AI-123-user-authentication
bugfix/AI-456-fix-response-formatting
hotfix/AI-789-security-vulnerability
```

### Creating a New Branch

Start all branches from the latest `main`:

```bash
# Ensure main is up to date
git checkout main
git pull

# Create and checkout new branch
git checkout -b feature/AI-123-user-authentication
```

## Commit Strategy

### Commit Message Format

Commit messages should follow this format:
```
[AI-123] Short descriptive summary (under 50 chars)

Detailed explanation of what changes were made and why.
Include any important context or considerations.
```

### Commit Best Practices

1. **Commit Frequently**: Make small, focused commits
2. **Atomic Commits**: Each commit should represent one logical change
3. **Reference Linear**: Always include the Linear ticket ID
4. **Descriptive Messages**: Write clear explanations of what and why (not how)
5. **Local Rebasing**: Clean up local commits before pushing
   ```bash
   # Squash or fixup messy commit history
   git rebase -i $(git merge-base HEAD main)  # Squash all commits since branching from main
   ```

## CI and GitHub Actions

Our CI pipeline automatically runs on every push and has these key checks:

1. **Linting**: Style and code quality checks
2. **Type Checking**: For type safety
3. **Unit Tests**: For individual components
4. **Integration Tests**: For component interactions
5. **Build Verification**: Ensures the project builds correctly

### CI Requirements for PR Approval

- All CI checks must pass
- Minimum 85% code coverage for new code
- No critical security vulnerabilities
- No performance regressions

## Rebase vs Merge: Our Approach

We follow a **rebase-based workflow** for these reasons:

1. **Linear History**: Maintains a clean, linear history
2. **Easier Debugging**: Makes `git bisect` more effective
3. **Cleaner Reverts**: Simplifies reverting features when needed
4. **Avoids Merge Commits**: No unnecessary merge commits cluttering history
5. **Better Feature Isolation**: Each feature is cleanly applied on top of main

### Keeping Feature Branches Updated

Regularly rebase feature branches on main:

```bash
git checkout feature/AI-123-user-authentication
git fetch origin
git rebase origin/main
# Resolve any conflicts
git push --force-with-lease  # Safe force push
```

## Pull Request Process

### When to Create a PR

Create a PR when:
1. Feature implementation is complete
2. All tests pass locally
3. Code meets our quality standards
4. You have written/updated documentation

### PR Template Elements

1. **Linear Link**: Link to the Linear ticket
2. **Description**: What the PR accomplishes
3. **Testing**: How the changes were tested
4. **Screenshots/Recordings**: For visual changes
5. **Checklist**: Quality assurance items

### PR Preparation

Before creating a PR:

```bash
# Ensure tests pass
npm run test

# Rebase on latest main
git fetch origin
git rebase origin/main

# Squash all commits on this branch into a single, well-crafted commit
git rebase -i $(git merge-base HEAD main)

# Push to remote
git push --force-with-lease
```

### PR Creation and Review Process

1. Create PR in GitHub targeting `main`
2. Use the PR template
3. Set appropriate reviewers
4. Address feedback by adding new commits
5. Once approved, maintainer or PR author merges using rebase strategy

### Merge Criteria

PRs are ready to merge when:
1. Required reviewers have approved
2. All CI checks pass
3. No unresolved conversations
4. Linear ticket is updated with implementation details
5. Documentation is updated

### Merge Strategy

We use GitHub's "Squash and merge" option which:
1. Combines all branch commits into a single commit
2. Creates a clean, focused entry in the main branch history
3. Maintains a linear history
4. Uses the PR title and description for the commit message
5. Preserves authorship information

Note: Since we already squash commits locally before PR creation, this is often redundant but ensures consistency in our main branch history.

### Post-Merge Cleanup

After a PR is merged:
1. The Linear ticket should be moved to "Done"
2. The branch should be deleted (automated by GitHub)
3. Local branches should be cleaned up:
   ```bash
   git checkout main
   git pull
   git branch -d feature/AI-123-user-authentication
   ```

## Special Cases

### Hotfixes for Production

1. Branch directly from the production tag/commit
2. Follow the `hotfix/AI-XXX-description` naming convention
3. After PR approval, merge to both `main` and the production branch
4. Tag the production branch with a version increment

### Long-Running Feature Branches

For features that take more than a few days:
1. Rebase on main daily
2. Consider creating a draft PR early for visibility
3. Break down into smaller incremental PRs when possible
4. Request early feedback via informal reviews

## Workflow Example

```
# Linear ticket AI-123: "Implement user authentication"

# 1. Create branch
git checkout main
git pull
git checkout -b feature/AI-123-user-authentication

# 2. Make changes and commit
# ... work, work, work ...
git add .
git commit -m "[AI-123] Add user authentication endpoints"

# ... more work ...
git add .
git commit -m "[AI-123] Add login form and client-side validation"

# 3. Prepare for PR
git fetch origin
git rebase origin/main
npm run test

# 4. Squash all branch commits into a single, well-crafted commit
git rebase -i $(git merge-base HEAD main)

# 5. Push to remote
git push --force-with-lease

# 6. Create PR in GitHub UI
# 7. Address review feedback with new commits
# 8. PR is approved and merged via GitHub "Rebase and merge"

# 9. Clean up
git checkout main
git pull
git branch -d feature/AI-123-user-authentication
```

By following this workflow, we maintain a clean repository history, ensure high code quality, and maximize team efficiency.