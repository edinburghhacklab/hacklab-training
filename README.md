# hacklab-training

Training syllabi for Edinburgh Hacklab.

If you're just looking for the content, see [training.ehlab.uk](https://training.ehlab.uk).

## Adding training

The training materials are generated from the markdown files in this repo, which are structured like this:

```
└── syllabuses
    └── <Location, ie Workshop>
        ├── <Tool, ie CNC Mill>
        │   ├── risk-assessment.md
        │   └── syllabus.md
```

`syllabus.md` becomes the training doc, and each header becomes an item in the training card. Each level 2 (`##`) header in `risk-assessment.md` becomes a row in the risk assessment, and the subheaders are used to populate the columns.

To preview your built changes locally, run `./scripts/open.sh` or ``./scripts/generate.sh` from the root of the repo. This requires docker to be working - if this is a problem consider using `shell.ehlab.uk`. You can also add a case insensitive filter to the end of the command to speed things up, ie `./scripts/generate.sh workshop`

If you're adding a new tool, run `./scripts/new-tool.sh <tool name> <tool location>`, ie `./scripts/new-tool.sh "CNC Mill" "Workshop"`

If you want to mess with the code that does the generation, see [`generator/README.md`](./generator/README.md)

### Common pitfalls

  - There may still be some cases where our generator doesn't escape special characters properly, which might break text containing any of: `\ % & $ # _ { } ~ ^`. If this seems to be the case, ask someone who's comfortable poking the generator to take a look.
  - When writing risk assessments, note that the subheaders need to have specific names in order to actually be included. These are case sensitive:
    - Severity
    - Likelihood
    - Risk rating
    - Who may be harmed & how
    - Control measures
