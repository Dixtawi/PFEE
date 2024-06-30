## Continuous Integration

Ce projet utilise GitHub Actions pour l'intégration continue.

### Configuration

Le workflow CI est défini dans `.github/workflows/ci.yml`.

### Validation des Messages de Commit

Les messages de commit doivent suivre ce format:
- `feat: Description de la fonctionnalité`
- `fix: Description de la correction`
- `docs: Description de la documentation`
- `style: Description des changements de style`
- `refactor: Description du refactoring`
- `test: Description des tests`
- `chore: Description des tâches de maintenance`

Un hook de validation des messages de commit est inclus et sera exécuté pendant le processus CI.

### Installation des Dépendances

```sh
pip install -r requirements.txt

