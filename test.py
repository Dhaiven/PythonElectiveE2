# FICHIER GENERE PAR IA JUSTE POUR FAIRE LES TESTS RECURSIF

import os
import subprocess
import sys


def run_doctests_with_cd(root_dir):
    print(f"🚀 Analyse récursive complète")
    print("=" * 60)

    for root, dirs, files in os.walk(root_dir):
        # On ignore les dossiers système/cache
        if any(ignored in root for ignored in ["__pycache__", ".git", ".pytest_cache", ".venv"]):
            continue

        for file in files:
            if file.endswith(".py") and file != os.path.basename(__file__):
                file_path = os.path.join(root, file)

                # Exécution du test
                result = subprocess.run(
                    [sys.executable, "-m", "doctest", "-v", file],
                    cwd=root,
                    capture_output=True,
                    text=True
                )

                # LOGIQUE D'AFFICHAGE AMÉLIORÉE
                output = result.stdout + result.stderr

                if "FAILED" in output or "********************************" in output:
                    print(f"\n❌ ERREUR : {file_path}")
                    print("-" * 40)
                    print(output)
                    print("-" * 40)
                elif "trying:" in output.lower():
                    # Si "trying" est présent, il y avait des tests et ils ont réussi
                    print(f"✅ TESTS OK : {file_path}")
                else:
                    # Le fichier a été scanné mais ne contient aucun test doctest
                    print(f"⚪ IGNORÉ (Pas de doctests) : {file_path}")


if __name__ == "__main__":
    run_doctests_with_cd(os.getcwd())