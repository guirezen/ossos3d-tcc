"""
Testes básicos para verificar se as bibliotecas estão funcionando corretamente.
"""

def test_numpy():
    try:
        import numpy as np
        arr = np.array([1, 2, 3])
        assert len(arr) == 3
        print("✅ NumPy funcionando")
        return True
    except ImportError:
        print("❌ Erro ao importar NumPy")
        return False
    
def test_pandas():
    try:
        import pandas as pd
        df = pd.DataFrame({'A': [1, 2, 3]})
        assert len(df) == 3
        print("✅ Pandas funcionando")
        return True
    except ImportError:
        print("❌ Erro ao importar Pandas")
        return False
    
def test_sklearn():
    try:
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.svm import SVC
        rf = RandomForestClassifier(n_estimators=10)
        svm = SVC()
        print("✅ Scikit-learn funcionando")
        return True
    except ImportError:
        print("❌ Erro ao importar Scikit-learn")
        return False

def test_trimesh():
    try:
        import trimesh
        # Criar uma esfera simples para teste
        sphere = trimesh.creation.uv_sphere(radius=1.0)
        assert sphere.vertices.shape[0] > 0
        print("✅ Trimesh funcionando")
        return True
    except ImportError:
        print("❌ Erro ao importar Trimesh")
        return False

def test_open3d():
    try:
        import open3d as o3d
        # Criar uma esfera simples para teste
        sphere = o3d.geometry.TriangleMesh.create_sphere(radius=1.0)
        assert len(sphere.vertices) > 0
        print("✅ Open3D funcionando")
        return True
    except ImportError:
        print("❌ Erro ao importar Open3D")
        return False

def test_matplotlib():
    try:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 4, 2])
        plt.close()
        print("✅ Matplotlib funcionando")
        return True
    except ImportError:
        print("❌ Erro ao importar Matplotlib")
        return False

def run_all_tests():
    print("=== Testando bibliotecas ===")
    tests = [
        test_numpy,
        test_pandas,
        test_sklearn,
        test_trimesh,
        test_open3d,
        test_matplotlib
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n=== Resumo ===")
    if all(results):
        print("✅ Todas as bibliotecas estão funcionando corretamente!")
    else:
        print("❌ Algumas bibliotecas apresentaram problemas.")
        print("Verifique a instalação e tente novamente.")

if __name__ == "__main__":
    run_all_tests()