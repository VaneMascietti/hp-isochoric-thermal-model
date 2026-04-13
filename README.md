# hp-isochoric-thermal-model

Reduced thermal–thermodynamic model for high-pressure isochoric experiments in the CO2 + n-hexadecane system.

This repository is structured around **one common simulation core** and **two execution modes**:

- **fit**: estimate effective model parameters from a selected experiment
- **predict**: reuse fitted parameters to simulate independent validation experiments

That architecture follows the project instruction to avoid duplicated logic and keep a single maintainable model engine. The model is intended to represent a **thermally non-uniform connected system** composed of the HP cell, the pressure line, and the upper region near the transducer. The measured pressure is therefore not treated as the pressure of a spatially uniform isochoric system.

## Scientific scope

The working hypothesis is a reduced three-node representation:

- Node 1: HP cell + contained fluid, with measured sample temperature `T1(t)`
- Node 2: vertical line region, strongly influenced by the external bath
- Node 3: upper region near fittings/transducer, represented by an effective dynamic temperature

Pressure is obtained from a mass-conservation closure over subvolumes at different local temperatures:

```text
m_tot = rho(P, T1, z) V1 + rho(P, T2, z) V2 + rho(P, T3, z) V3
```

The effective parameters to be fitted are intentionally reduced, for example:

- `tau3_s`: effective thermal time constant of the upper region
- `lambda_env`: coupling weight of the upper region to line/environment
- `V3_ml`: effective correction for the upper subvolume within geometric bounds

## Repository layout

```text
hp-isochoric-thermal-model/
├── README.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── configs/
├── data/
├── src/hpmodel/
├── scripts/
├── results/
├── notebooks/
└── tests/
```

## Suggested workflow

1. Define geometry and experiment metadata in YAML files.
2. Read raw LabVIEW `.lvm` files.
3. Standardize columns and preprocess signals.
4. Fit effective parameters using one experiment (for example Exp. 6).
5. Reuse fitted parameters to predict another experiment (for example Exp. 7).
6. Compare simulated and experimental pressure trajectories.

## First commands

Create an environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

Run a fit:

```bash
python scripts/run_fit.py --config configs/fit_exp06.yaml
```

Run a prediction:

```bash
python scripts/run_predict.py --config configs/predict_exp07.yaml --params results/fits/example_fit.json
```

## Current status

This scaffold includes:

- config templates
- a minimal package structure
- placeholders for EOS, thermal model, pressure solver, fitting, and plotting
- command-line entry scripts
- small starter tests

It is meant to be a clean starting point for the reduced model described in the project notes.
