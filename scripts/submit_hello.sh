#!/bin/bash
#SBATCH --job-name=helloworld
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G
#SBATCH --time=00:01:00
#SBATCH --output=logs/%j.out

module load apptainer

mkdir -p data/final

export APPTAINER_ENV_OUTPUT_DIR="data/final"

apptainer exec \
  --bind .:/app \
  --pwd /app \
  --env PYTHONPATH="/app/src" \
  ./containers/env.sif \
  /opt/venv/bin/python scripts/say_hello.py
