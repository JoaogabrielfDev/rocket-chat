import subprocess
import os
import sys
from pathlib import Path

def run_backend():
    """Inicia o backend"""
    backend_dir = Path(__file__).parent / "backend"
    print("🚀 Iniciando backend...")
    subprocess.run(
        [sys.executable, "run.py"],
        cwd=backend_dir,
        check=False
    )

def run_frontend():
    """Inicia o frontend"""
    frontend_dir = Path(__file__).parent / "frontend"
    print("🎨 Iniciando frontend...")
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", "main.py"],
        cwd=frontend_dir,
        check=False
    )

if __name__ == "__main__":
    import threading
    
    # Iniciar backend em uma thread separada
    backend_thread = threading.Thread(target=run_backend, daemon=True)
    backend_thread.start()
    
    # Iniciar frontend em uma thread separada
    frontend_thread = threading.Thread(target=run_frontend, daemon=True)
    frontend_thread.start()
    
    print("\n✅ Frontend e Backend iniciados!")
    print("Frontend: http://localhost:8501")
    print("Backend: (verifique o terminal para detalhes)\n")
    
    # Manter o script rodando
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n\n🛑 Encerrando aplicação...")
        sys.exit(0)
