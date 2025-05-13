"""
Configurações do projeto
"""

import os
from pathlib import Path

# Diretórios do projeto
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
MODELS_DIR = OUTPUTS_DIR / "models"
FEATURES_DIR = OUTPUTS_DIR / "features"
VISUALIZATIONS_DIR = OUTPUTS_DIR / "visualizations"

# Configurações de processamento
MESH_REDUCTION_FACTOR = 0.9  # 90% de redução
RANDOM_STATE = 42

# Configurações de modelos
N_ESTIMATORS_RF = 100
CV_FOLDS = 5

# Criar diretórios se não existirem
for directory in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, 
                  OUTPUTS_DIR, MODELS_DIR, FEATURES_DIR, VISUALIZATIONS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

print("✅ Configuração inicial concluída!")