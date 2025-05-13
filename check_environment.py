"""
Script de verificação completa do ambiente do projeto
Executa todos os testes e validações necessárias
"""

import os
import sys
import subprocess
from pathlib import Path
import json
from datetime import datetime

class EnvironmentChecker:
    def __init__(self):
        self.project_root = Path.cwd()
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'python_version': sys.version,
            'checks': {}
        }
    
    def check_python_version(self):
        """Verificar versão do Python"""
        version = sys.version_info
        if version.major == 3 and version.minor >= 8:
            self.results['checks']['python_version'] = {
                'status': 'success',
                'message': f'Python {version.major}.{version.minor}.{version.micro} ✅',
                'details': sys.version
            }
            return True
        else:
            self.results['checks']['python_version'] = {
                'status': 'error',
                'message': f'Python {version.major}.{version.minor} ❌ (Requerido: 3.8+)',
                'details': sys.version
            }
            return False
    
    def check_virtual_environment(self):
        """Verificar se está em um ambiente virtual"""
        if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            self.results['checks']['virtual_env'] = {
                'status': 'success',
                'message': 'Ambiente virtual ativo ✅',
                'details': f'Prefix: {sys.prefix}'
            }
            return True
        else:
            self.results['checks']['virtual_env'] = {
                'status': 'warning',
                'message': 'Ambiente virtual não detectado ⚠️',
                'details': 'Recomendado usar um ambiente virtual'
            }
            return False
    
    def check_project_structure(self):
        """Verificar estrutura do projeto"""
        expected_dirs = ['src', 'data', 'notebooks', 'tests', 'outputs']
        expected_files = ['requirements.txt', 'README.md', '.gitignore']
        
        missing_dirs = []
        missing_files = []
        
        for directory in expected_dirs:
            if not (self.project_root / directory).exists():
                missing_dirs.append(directory)
        
        for file in expected_files:
            if not (self.project_root / file).exists():
                missing_files.append(file)
        
        if not missing_dirs and not missing_files:
            self.results['checks']['project_structure'] = {
                'status': 'success',
                'message': 'Estrutura do projeto completa ✅',
                'details': {'dirs': expected_dirs, 'files': expected_files}
            }
            return True
        else:
            self.results['checks']['project_structure'] = {
                'status': 'error',
                'message': 'Estrutura do projeto incompleta ❌',
                'details': {
                    'missing_dirs': missing_dirs,
                    'missing_files': missing_files
                }
            }
            return False
    
    def check_installed_packages(self):
        """Verificar pacotes instalados"""
        required_packages = [
            'numpy', 'pandas', 'scikit-learn', 'matplotlib', 
            'seaborn', 'trimesh', 'open3d', 'jupyter'
        ]
        
        installed = []
        missing = []
        
        for package in required_packages:
            try:
                __import__(package)
                installed.append(package)
            except ImportError:
                missing.append(package)
        
        if not missing:
            self.results['checks']['packages'] = {
                'status': 'success',
                'message': 'Todos os pacotes essenciais instalados ✅',
                'details': {'installed': installed}
            }
            return True
        else:
            self.results['checks']['packages'] = {
                'status': 'error',
                'message': f'{len(missing)} pacotes faltando ❌',
                'details': {
                    'installed': installed,
                    'missing': missing
                }
            }
            return False
    
    def check_scripts_syntax(self):
        """Verificar sintaxe dos scripts Python"""
        python_files = list(self.project_root.glob('src/*.py'))
        python_files.extend(list(self.project_root.glob('tests/*.py')))
        
        valid_files = []
        invalid_files = []
        
        for file_path in python_files:
            try:
                with open(file_path, 'r') as f:
                    compile(f.read(), file_path, 'exec')
                valid_files.append(str(file_path.relative_to(self.project_root)))
            except SyntaxError as e:
                invalid_files.append({
                    'file': str(file_path.relative_to(self.project_root)),
                    'error': str(e)
                })
            except Exception as e:
                invalid_files.append({
                    'file': str(file_path.relative_to(self.project_root)),
                    'error': f'Erro ao ler arquivo: {e}'
                })
        
        if not invalid_files:
            self.results['checks']['scripts_syntax'] = {
                'status': 'success',
                'message': 'Todos os scripts têm sintaxe válida ✅',
                'details': {'valid_files': valid_files}
            }
            return True
        else:
            self.results['checks']['scripts_syntax'] = {
                'status': 'error',
                'message': f'{len(invalid_files)} arquivos com problemas ❌',
                'details': {
                    'valid_files': valid_files,
                    'invalid_files': invalid_files
                }
            }
            return False
    
    def run_library_tests(self):
        """Executar testes das bibliotecas"""
        test_script = self.project_root / 'tests' / 'test_libraries.py'
        
        if not test_script.exists():
            self.results['checks']['library_tests'] = {
                'status': 'error',
                'message': 'Script de teste não encontrado ❌',
                'details': f'{test_script} não existe'
            }
            return False
        
        try:
            # Executar script de teste
            result = subprocess.run(
                [sys.executable, str(test_script)],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                self.results['checks']['library_tests'] = {
                    'status': 'success',
                    'message': 'Todos os testes de biblioteca passaram ✅',
                    'details': {
                        'stdout': result.stdout,
                        'stderr': result.stderr
                    }
                }
                return True
            else:
                self.results['checks']['library_tests'] = {
                    'status': 'error',
                    'message': 'Alguns testes falharam ❌',
                    'details': {
                        'return_code': result.returncode,
                        'stdout': result.stdout,
                        'stderr': result.stderr
                    }
                }
                return False
        except subprocess.TimeoutExpired:
            self.results['checks']['library_tests'] = {
                'status': 'error',
                'message': 'Teste expirou (timeout) ❌',
                'details': 'Testes demoraram mais que 60 segundos'
            }
            return False
        except Exception as e:
            self.results['checks']['library_tests'] = {
                'status': 'error',
                'message': f'Erro ao executar testes ❌',
                'details': str(e)
            }
            return False
    
    def save_report(self):
        """Salvar relatório de verificação"""
        report_path = self.project_root / 'environment_check_report.json'
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        print(f"\n📝 Relatório salvo em: {report_path}")
    
    def print_summary(self):
        """Imprimir resumo dos resultados"""
        print("\n" + "="*60)
        print("RESUMO DA VERIFICAÇÃO DO AMBIENTE")
        print("="*60)
        
        success_count = 0
        total_checks = len(self.results['checks'])
        
        for check_name, check_result in self.results['checks'].items():
            status = check_result['status']
            message = check_result['message']
            
            print(f"\n{check_name.replace('_', ' ').title()}:")
            print(f"  {message}")
            
            if status == 'success':
                success_count += 1
            elif status == 'error':
                if 'details' in check_result:
                    details = check_result['details']
                    if isinstance(details, dict):
                        for key, value in details.items():
                            if isinstance(value, list) and value:
                                print(f"    {key}: {', '.join(map(str, value))}")
                            elif not isinstance(value, list):
                                print(f"    {key}: {value}")
        
        print("\n" + "="*60)
        print(f"RESULTADO FINAL: {success_count}/{total_checks} verificações passaram")
        
        if success_count == total_checks:
            print("🎉 AMBIENTE TOTALMENTE CONFIGURADO!")
            print("   Você pode prosseguir para a Parte 2 do projeto.")
        else:
            print("⚠️  ALGUNS PROBLEMAS ENCONTRADOS")
            print("   Resolva os problemas acima antes de continuar.")
            return False
        
        print("="*60)
        return True
    
    def run_all_checks(self):
        """Executar todas as verificações"""
        print("🔍 Iniciando verificação do ambiente...")
        
        checks = [
            ('Versão do Python', self.check_python_version),
            ('Ambiente Virtual', self.check_virtual_environment),
            ('Estrutura do Projeto', self.check_project_structure),
            ('Pacotes Instalados', self.check_installed_packages),
            ('Sintaxe dos Scripts', self.check_scripts_syntax),
            ('Testes das Bibliotecas', self.run_library_tests)
        ]
        
        for check_name, check_function in checks:
            print(f"\n📋 Verificando: {check_name}...")
            success = check_function()
            if success:
                print(f"   ✅ {check_name} - OK")
            else:
                print(f"   ❌ {check_name} - Problema detectado")
        
        self.save_report()
        return self.print_summary()

def main():
    """Função principal"""
    checker = EnvironmentChecker()
    success = checker.run_all_checks()
    
    if success:
        print("\n🚀 Próximo passo: Execute os notebooks em notebooks/ para começar o desenvolvimento!")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())