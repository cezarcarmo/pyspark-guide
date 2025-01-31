# Guia de Boas Práticas com Git

Este documento descreve as melhores práticas para versionamento de código no projeto **Guia Completo de PySpark**.

## 📌 Estrutura de Branches

Para manter o código organizado e facilitar a colaboração, seguimos esta estrutura de branches:

- `main` → Versão estável do projeto.
- `develop` → Desenvolvimento contínuo.
- `feature/nome-da-feature` → Implementação de novas funcionalidades.
- `fix/nome-do-fix` → Correção de bugs.

## 🚀 Fluxo de Trabalho no Git

### 1️⃣ **Clonando o Repositório**
```bash
git clone https://github.com/seu-usuario/pyspark-guide.git
cd pyspark-guide
```

### 2️⃣ **Criando uma Branch para uma Nova Feature**
```bash
git checkout -b feature/nova-feature
```

### 3️⃣ **Fazendo Commits Pequenos e Descritivos**
```bash
git add .
git commit -m "Adiciona script de leitura de dados CSV no PySpark"
```

### 4️⃣ **Mantendo a Branch Atualizada**
Antes de subir código, atualize sua branch com a versão mais recente do `develop`:
```bash
git pull origin develop
```

### 5️⃣ **Enviando as Alterações para o GitHub**
```bash
git push origin feature/nova-feature
```

### 6️⃣ **Abrindo um Pull Request (PR)**
1. Acesse o repositório no GitHub.
2. Vá para a aba **Pull Requests**.
3. Clique em **New Pull Request** e selecione `develop` como destino.
4. Adicione uma descrição clara sobre as mudanças.
5. Solicite revisão antes de fazer o merge.

### 7️⃣ **Finalizando a Feature**
Após a aprovação e merge do Pull Request:
```bash
git checkout develop
git pull origin develop
git branch -d feature/nova-feature
```

## 🔥 Checklist para Commits de Qualidade
✅ **Pequenos e focados** em uma única mudança.
✅ **Mensagens claras**, explicando o que foi feito.
✅ **Código testado** antes do commit.
✅ **Não subir arquivos desnecessários** (`.gitignore` bem configurado).

---

Seguindo esse fluxo, garantimos um código bem estruturado e fácil de manter! 🚀

