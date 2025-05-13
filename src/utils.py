"""
Funções utilitárias para o projeto
"""

import os
import json
from pathlib import Path
from datetime import datetime
import logging

def setup_logging(log_level=logging.INFO):
    """Configurar logging para o projeto"""
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('project.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def save_json(data, filename):
    """Salvar dados em formato JSON"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
        
def load_json(filename):
    """Carregar dados do arquivo JSON"""
    with open(filename, 'r') as f:
        return json.load(f)
    
def create_timestamp():
    """Criar um timestamp para arquivos"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def validate_obj_file(filepath):
    """Verificar se um arquivo .obj é válido"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            has_vertices = 'v' in content
            has_faces = 'f' in content
            return has_vertices and has_faces
    except:
        return False
    
logger = setup_logging()