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
- `<linear-id>` is the Linear ticket ID (e.g., CRA-123)
- `<short-description>` is a brief, kebab-case description

Examples:
```
feature/CRA-123-user-authentication
bugfix/CRA-456-fix-response-formatting
hotfix/CRA-789-security-vulnerability
```

### Creating a New Branch

Start all branches from the latest `main`:

```bash
# Ensure main is up to date
git checkout main
git pull

# Create and checkout new branch
git checkout -b feature/CRA-123-user-authentication
```

## Commit Strategy

### Commit Message Format

Commit messages should follow this format:
```
[CRA-123] Short descriptive summary (under 50 chars)

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

As our CI pipeline evolves, we'll implement these key checks:

1. **Basic Linting**: Essential style and code quality rules
2. **Type Checking**: Where applicable
3. **Critical Tests**: Focus on core functionality
4. **Build Verification**: Ensures the project builds correctly

### CI Requirements for PR Approval

- All implemented CI checks must pass
- No critical security vulnerabilities
- PRs should not degrade existing functionality

### Linting Philosophy

We follow a minimalist approach to linting:
- Focus on functionality-impacting issues, not stylistic preferences
- Implement only rules with clear value and broad agreement
- Automatically fix formatting issues where possible
- Document exceptions when breaking rules is necessary

### Local Verification Before Push

Always run these checks locally before pushing:
```bash
# Run whatever linting and testing tools are set up for the project
# For example (actual commands will vary based on our toolchain):
./scripts/lint.sh
./scripts/test.sh
```

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
git checkout feature/CRA-123-user-authentication
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
# Verify code quality locally (specific commands depend on project tooling)
# Run any established linting/testing scripts

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
   git branch -d feature/CRA-123-user-authentication
   ```

## Special Cases

### Hotfixes for Production

1. Branch directly from the production tag/commit
2. Follow the `hotfix/CRA-XXX-description` naming convention
3. After PR approval, merge to both `main` and the production branch
4. Tag the production branch with a version increment

### Long-Running Feature Branches

For features that take more than a few days:
1. Rebase on main daily
2. Consider creating a draft PR early for visibility
3. Break down into smaller incremental PRs when possible
4. Request early feedback via informal reviews

## Branch Coordination Process

To prevent conflicts from multiple branches modifying the same files:

### 1. Pre-Work Coordination

Before creating a new ticket or branch:
- Check active branches and PRs to identify which files are being modified
- Review Linear for related tickets that might involve the same files
- Document potential conflict areas with other in-progress work

### 2. Work Allocation Guidelines

- Prioritize sequential rather than parallel work on the same files
- Wait for related work to be merged when modifications would overlap
- For unavoidable parallel work, establish clear boundaries within files
- Document dependencies between tickets explicitly in Linear

### 3. Branch Creation Protocol

- Create ticket with clear scope boundaries
- Document potential file overlap with existing tickets in the description
- If overlap exists, add "Depends on" or "Related to" links in Linear
- Include conflict avoidance strategy in the ticket description
- Create branch only when prerequisites are met

### 4. Regular Synchronization

- Update local branch from main at least daily
- Track active work in team communication channels
- Conduct periodic reviews of active branches (weekly)
- Identify and address emerging conflicts early through communication

### 5. Conflict Prevention Strategies

- Structure code with clear component boundaries
- Use interfaces to minimize implementation coupling
- Break large features into smaller, independent PRs
- When editing shared files, focus on distinct sections
- Consider temporary feature flags for parallel development

### 6. Merge Prioritization

- Establish clear order for merging dependent branches
- Prioritize PRs that unblock other work
- Create explicit dependency chains in Linear
- Regularly review PR queue to optimize merge order

## Complete Workflow Process

### Starting Work on a Ticket

1. **Check ticket status and prerequisites**
   - Verify ticket is not blocked by other work
   - Check if any dependent tickets need to be completed first
   - Review ticket details and requirements

2. **Perform branch coordination check**
   - Identify potential file conflicts with existing branches
   - Determine if work should be deferred or modified to avoid conflicts
   - Document coordination strategy if overlap exists

3. **Create local branch**
   - Ensure branch follows naming convention: `<type>/CRA-XX-description`
   - Branch from latest main
   - Push branch to remote with tracking

4. **Update ticket status**
   - Move ticket to "In Progress" in Linear
   - Assign to self if not already assigned
   - Update ticket with branch name for reference

### Switching Between Work Items

1. **Save current state**
   - Commit all work-in-progress changes with [WIP] prefix
   - Document current status in Linear ticket
   - Push changes to remote branch

2. **Prepare for switch**
   - Clean working directory (stash any uncommitted changes)
   - Document exact stopping point with detailed notes

3. **Activate new context**
   - Checkout target branch (create if needed)
   - Pull latest changes from remote
   - Review ticket details and requirements

4. **Update work tracking**
   - Update both tickets with context switch information
   - Set appropriate status in Linear (Paused, Blocked, etc.)

### Completing Work on a Ticket

1. **Finalize implementation**
   - Clean up code (remove debug statements, etc.)
   - Apply consistent formatting
   - Add or update documentation
   - Complete final tests

2. **Prepare commits**
   - Ensure all commits reference ticket "[CRA-XX]"
   - Squash WIP commits into logical units
   - Use descriptive commit messages

3. **Final verification**
   - Run linting and static analysis tools
   - Execute all tests relevant to changes
   - Check against acceptance criteria

4. **Create pull request**
   - Push final changes to remote
   - Set appropriate reviewers
   - Link PR to Linear ticket

5. **Update ticket status**
   - Move ticket to "In Review" or equivalent status
   - Add PR link to ticket
   - Document any testing notes or special considerations

## Workflow Example

```
# Linear ticket CRA-123: "Implement user authentication"

# 1. Start work on ticket
git checkout main
git pull
git checkout -b feature/CRA-123-user-authentication

# 2. Make changes and commit
# ... work, work, work ...
git add .
git commit -m "[CRA-123] Add user authentication endpoints"

# ... more work ...
git add .
git commit -m "[CRA-123] Add login form and client-side validation"

# 3. Prepare for PR
git fetch origin
git rebase origin/main
# Run local quality checks (whatever is established for the project)

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
git branch -d feature/CRA-123-user-authentication
```

By following this workflow, we maintain a clean repository history, ensure high code quality, minimize merge conflicts, and maximize team efficiency.