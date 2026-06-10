# Hackathon Workspace — private materials

Everything in this folder is **private** and must never reach the public fork.

```
hackathon/
├── README.md     ← this file
├── notes/        ← running notes, scratch, meeting notes
├── prds/         ← product requirement docs
└── research/     ← references, links, datasets, emissions data
```

## Day-to-day workflow

You work entirely against the **private** `origin` (`Concepcion-c/TRACE`):

```bash
git add -A
git commit -m "..."
git push origin trunk          # or your feature branch
```

All branches and the `hackathon/` notes live here, safely private.

## Pulling upstream CCF updates

```bash
git fetch upstream
git merge upstream/trunk        # or rebase, your call
```

## Publishing the final project to the public fork

The public fork (`Concepcion-c/cloud-carbon-footprint`) is **world-visible**, so we
publish a curated branch that has the `hackathon/` folder removed. Run this only when
you're ready to expose the final result.

```bash
# 1. Make sure trunk is committed and clean.
git checkout trunk

# 2. Create a clean publish branch from trunk.
git checkout -B publish

# 3. Remove private materials from this branch only.
git rm -r --cached hackathon
git commit -m "Publish: strip private hackathon materials"

# 4. Push to the public fork's trunk.
git push public publish:trunk

# 5. Return to your working branch.
git checkout trunk
```

> Double-check before step 4: `git show publish:hackathon/README.md` should error
> ("path does not exist"), confirming notes are not in the published tree.

Alternatively, open a PR from the fork's `trunk` to the upstream org repo via the
GitHub UI once the fork is updated.
