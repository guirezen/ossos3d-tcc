#!/bin/bash

# Script SEGURO para configuração do projeto
# Não sobrescreve arquivos existentes

echo "🚀 Configurando projeto TCC - Ossos 3D (modo seguro)..."

# 1. Criar estrutura de pastas (mkdir -p não apaga pastas existentes)
echo "📁 Criando estrutura de pastas..."
mkdir -p data/{raw,processed}
mkdir -p src
mkdir -p notebooks
mkdir -p tests
mkdir -p outputs/{models,features,visualizations}
mkdir -p docs
mkdir -p .vscode

# 2. Criar arquivos __init__.py (apenas se não existirem)
echo "🐍 Criando arquivos Python..."
[ ! -f src/__init__.py ] && touch src/__init__.py
[ ! -f tests/__init__.py ] && touch tests/__init__.py

# 3. Criar requirements.txt (apenas se não existir)
if [ ! -f "requirements.txt" ]; then
    echo "📦 Criando requirements.txt..."
    cat > requirements.txt << 'EOL'
# Core libraries
numpy>=1.21.0
pandas>=1.3.0
scipy>=1.7.0

# Machine Learning
scikit-learn>=1.0.0
xgboost>=1.5.0
lightgbm>=3.2.0

# 3D Processing
trimesh>=3.10.0
open3d>=0.15.0
meshio>=5.3.0

# Visualization
matplotlib>=3.4.0
seaborn>=0.11.0
plotly>=5.5.0

# Data Processing
PyYAML>=6.0
tqdm>=4.62.0

# Development
jupyter>=1.0.0
jupyterlab>=3.0.0
notebook>=6.4.0

# Testing
pytest>=6.2.0
pytest-cov>=3.0.0

# Utils
python-dotenv>=0.19.0
EOL
else
    echo "⚠️  requirements.txt já existe - mantendo versão atual"
fi

# 4. Criar .gitignore (apenas se não existir)
if [ ! -f ".gitignore" ]; then
    echo "🔒 Criando .gitignore..."
    cat > .gitignore << 'EOL'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Jupyter Notebook
.ipynb_checkpoints

# Data files
data/raw/*.obj
data/raw/*.ply
data/processed/*.obj
data/processed/*.ply

# Output files
outputs/models/*.pkl
outputs/models/*.joblib
outputs/features/*.csv
outputs/visualizations/*.png
outputs/visualizations/*.pdf

# Logs
*.log

# OS
.DS_Store
Thumbs.db
EOL
else
    echo "⚠️  .gitignore já existe - mantendo versão atual"
fi

# 5. Criar configuração do VS Code (apenas se não existir)
if [ ! -f ".vscode/settings.json" ]; then
    echo "⚙️ Configurando VS Code..."
    cat > .vscode/settings.json << 'EOL'
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length=88"],
    "python.linting.pylintArgs": [
        "--max-line-length=88"
    ],
    "files.autoSave": "onFocusChange",
    "editor.formatOnSave": true,
    "jupyter.defaultKernel": "python3"
}
EOL
else
    echo "⚠️  .vscode/settings.json já existe - mantendo versão atual"
fi

# 6. Criar README.md (apenas se não existir)
if [ ! -f "README.md" ]; then
    echo "📖 Criando README.md..."
    cat > README.md << 'EOL'
# TCC: Aplicação de IA para Identificação de Padrões Anatômicos em Modelos 3D de Ossos

## Descrição
Sistema que utiliza técnicas de inteligência artificial para identificar e classificar padrões anatômicos em modelos 3D de ossos, com foco em estimativa de dimorfismo sexual e detecção de landmarks anatômicos.

## Estrutura do Projeto
```
ossos3d-tcc/
├── src/              # Código fonte
├── data/             # Dados (raw e processados)
├── notebooks/        # Jupyter notebooks
├── tests/            # Testes
├── outputs/          # Resultados
└── docs/             # Documentação
```

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente: `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows)
4. Instale as dependências: `pip install -r requirements.txt`

## Como usar

1. Configure o ambiente seguindo as instruções de instalação
2. Execute os testes: `python tests/test_libraries.py`
3. Siga os notebooks na ordem numérica

## Autor
Luiz Guilherme Rezende Paes

## Orientador
Victor Flávio de Andrade Araujo
EOL
else
    echo "⚠️  README.md já existe - mantendo versão atual"
fi

echo ""
echo "✅ Configuração concluída!"
echo ""
echo "📋 Resumo do que foi feito:"
echo "  - Pastas criadas/verificadas (preservadas se já existissem)"
echo "  - Arquivos criados apenas se não existissem"
echo "  - Nenhum arquivo existente foi sobrescrito"
echo ""
echo "Próximos passos:"
echo "1. Crie o ambiente virtual: python -m venv venv"
echo "2. Ative o ambiente: source venv/bin/activate (Linux/Mac) ou venv\\Scripts\\activate (Windows)"
echo "3. Instale as dependências: pip install -r requirements.txt"
echo "4. Execute os testes: python tests/test_libraries.py"