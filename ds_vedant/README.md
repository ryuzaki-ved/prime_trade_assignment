ds_vedant

This folder contains the organized structure for the candidate work in a Colab-friendly layout.

Structure created:

- `notebook_1.ipynb` — primary Colab notebook (wrapper, points to the original notebook)
- `notebook_2.ipynb` — optional secondary Colab notebook (wrapper)
- `csv_files/` — place to store CSVs and processed data
- `outputs/` — place to store images, charts, and other visual outputs
- `ds_report.pdf` — placeholder for final report

How to use

1. Inspect the repository and confirm which notebooks and CSVs you want moved.
2. Run the helper script `organize_files.py` from the repository root to copy files into this structure.

Example (dry run):

    python organize_files.py --candidate vedant --dry-run

To actually copy files run with `--execute`.

Notes

- This README and the wrapper notebooks are non-destructive. The helper script defaults to copying files so originals remain.
- If you'd like, I can run the script now to move files — tell me to proceed and whether to do a dry-run or an actual move.
