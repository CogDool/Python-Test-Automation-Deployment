import subprocess
import sys

def run_test_suite():
    print("Running Automated Tests...")
    # sys.executable dynamically points to the currently running Python interpreter
    result = subprocess.run([sys.executable, "-m", "pytest"], capture_output=True, text=True)
    return result.returncode == 0

def execute_deployment():
    print("Deploying to Production Server...")
    # Calls remote delivery tooling
    return True

if __name__ == "__main__":
    if run_test_suite():
        print("Tests Passed!")
        execute_deployment()
    else:
        print("Tests Failed. Deployment aborted.")
        sys.exit(1)

